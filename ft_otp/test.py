#!/usr/bin/env python3

import argparse
import os
import base64
import hashlib
import struct
import time
import pyotp
import re
import hmac
import time
import qrcode
from PIL import Image
#from imgcat import imgcat

def main():
	arg = ft_parser()
	if arg.g:
		file = ft_open(0, arg.g)
		encrypt = ft_encrypt(file)
		ft_save(encrypt, "ft_otp.key")
	if arg.k:
		encrypt = ft_open(1, arg.k).strip()
	otp = ft_generate(encrypt)
	totp = ft_totp(encrypt)
#	imgcat(img.tobytes())
	print("OTP: ", otp)
	print("TOTP: ",totp)

def ft_parser():
	parser = argparse.ArgumentParser(
		prog = 'ft_otp',
		description = 'Time One-Time Password'
		)
	exclude = parser.add_mutually_exclusive_group(required=True)
	exclude.add_argument('-g', metavar='FILE', help='Receive as an argument a hexadecimal key of at least 64 characters and safely store this key in a file called ft_otp.key')
	exclude.add_argument('-k' , metavar='FILE', help='Generate a new temporary password')
	return parser.parse_args()

def ft_open(control, source):
	try:
		with open(source, 'r') as f:
			file = f.read()
	except:
		ft_error(0)
	else:
		if not control and (len(file) < 64 or not re.match("^[0-9a-fA-F]+$", file)):
			ft_error(1)
	return file

def ft_encrypt(file):
	key = file.encode('utf-8')
	salt = os.urandom(16)
	key_hash = hashlib.sha256(salt + key).digest()
	mac = hmac.new(key_hash, salt, hashlib.sha256).digest()
	return base64.b64encode(salt + mac + key).decode('utf-8')

def ft_save(key, path):
	try:
		with open(path, 'w') as file:
			file.write(key)
		print("Key was successfully saved in",path)
	except:
		ft_error(2)

def ft_generate(key):
	now = int(time.time())
	alive = 30
	time_step = now // alive
	time_bytes = struct.pack('>Q', time_step)
	key_bytes = key.encode('utf-8')
	hmac_code = hmac.new(key_bytes, time_bytes,hashlib.sha1).digest()
	offset = hmac_code[-1] & 0x0F
	otp_unpack = struct.unpack('>I', hmac_code[offset:offset+4])[0] & 0x7FFFFFFF
	otp = str(otp_unpack % 1000000).zfill(6)
	return otp

def ft_totp(key):
	totp = pyotp.TOTP(base64.b32encode(key.encode()))
	return totp.now()

def ft_qr(otp):
	qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)
	qr.add_data(otp)
	qr.make(fit=True)
	img = qr.make_image(fill_color='black', back_color='white')
	img.show()
	return img

def ft_error(num):
	error = [
		"can't read or open file.",
		"key must be hexadecimal at least 64 characters",
		"can't save key to file"
		]

	if num < len(error):
		print("Error: ",error[num])
	else:
		print("Error don't found.")
	exit()

if __name__ == '__main__':
	main()