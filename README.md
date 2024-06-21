# Caesar Cipher Tool

This is a simple Caesar Cipher text encryption and decryption tool implemented in Python. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.This program allow users to input a message and a shift value to perform encryption or decryption of their choice.

## Requirements

Make sure you have Python3 installed on your system. If not, follow the instructions below to install it.

#### On Kali Linux
Kali Linux is a Debian-based distribution, so you can install Python 3 using apt.
````
sudo apt install python3
````
## How To Use
#### Clone the Repository:
````
https://github.com/sabrii6/PRODIGY_CS_01.git
````
#### Navigate to the Directory:
````
cd PRODIGY_CS_01
````
#### Run the Script:
````
python3 caeser.py
````
## Main Program
The ' main() ' function provides a simple command-line interface that allows the user to choose between encrypting and decrypting messages or exiting the program.

## Example
This is a simple example demonstrating the usage of the Caesar Cipher encrypt/decrypt tool implemented in Python.
````
Welcome to Cipher Encrypt/Decrypt Tool!!!

1.Encrypt Message
2.Decrypt Message
3.Exit

Enter your choice: 1
Enter the message to encrypt: prodigy
Enter the shift (a number between 1 and 25): 5
Encrypted Message: utwjnld

Do you want to perform another operation? (yes/no): yes       <!--- if u enter no the program will exit automatically --->  

1.Encrypt Message
2.Decrypt Message
3.Exit

Enter your choice: 2
Enter the message to decrypt: utwjnld
Enter the shift used for encryption: 5
Decrypted Message: prodigy

Do you want to perform another operation? (yes/no): yes

1.Encrypt Message
2.Decrypt Message
3.Exit

Enter your choice: 3
Exiting...
````
