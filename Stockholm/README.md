Stockholm Ransomware Simulator
Overview
Stockholm is a Python-based simulator for a ransomware attack, designed for educational purposes. It demonstrates how ransomware works by encrypting files with a generated key and simulating the decryption process. This project is intended for use in understanding encryption, decryption processes, and the potential impact of ransomware attacks on systems.

Features
Simulates the behavior of a ransomware attack by encrypting files with a randomly generated key.
Demonstrates the decryption process using a provided key.
Targets specific file extensions listed in wannacry_ext.txt.
Provides options for silent operation and reverse decryption.
Getting Started
Prerequisites

Installation
To run the Stockholm ransomware simulator, follow these steps:

Clone the repository to your local machine.
Navigate to the project directory.
Ensure you have Docker installed on your system. The project utilizes Docker for containerization.
Build the Docker image by running make build in the terminal.
Run the Docker container with make run. This will start the simulator in a Docker container.

Usage
After starting the simulator, you can interact with it through the command line interface. Here are some basic commands:

To simulate an encryption attack, simply run the simulator without any arguments.
To decrypt files, provide the -r argument followed by the decryption key.
Use the -s flag for silent operation, suppressing output messages.
To see available commands and options, use the -h flag for help.
To see the version of the project use the -v flag.

Contributing
Contributions to the Stockholm project are welcome. Please feel free to submit pull requests or report issues.

License
This project is licensed under the MIT License. See the LICENSE file for details.

This README provides a comprehensive introduction to the Stockholm project, including its purpose, features, installation instructions, usage guide, contribution guidelines, and licensing information. Adjustments can be made based on further project developments or specific requirements.