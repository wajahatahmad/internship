Caesar Cipher Encryption and Decryption Program

Overview

This Python program implements the Caesar Cipher algorithm, a classical encryption technique where each letter in a message is shifted by a fixed number of positions in the alphabet. The program allows users to input a message and a shift value to either encrypt or decrypt the text.

Features

Encryption: Convert plaintext into ciphertext by shifting each letter by a specified number of positions.

Decryption: Convert ciphertext back into plaintext using the same shift value used for encryption.

User Interaction: Users can input their message, specify the shift value, and choose whether to encrypt or decrypt the message.

Usage

Input:

Message: The text to be encrypted or decrypted.

Shift Value: An integer representing the number of positions each letter should be shifted.

Operation: Specify whether to encrypt or decrypt the message.

Process:

Encryption: Shifts each letter in the plaintext message forward by the given shift value within the alphabet.

Decryption: Shifts each letter in the ciphertext message backward by the given shift value to retrieve the original plaintext.

Output:

Encrypted Message: The result of applying the Caesar Cipher encryption to the input message.

Decrypted Message: The result of applying the Caesar Cipher decryption to the encrypted message, which should match the original plaintext if the correct shift value is used.

example:-

Enter the message: Hello, World!

Enter the shift value (integer): 3

Do you want to encrypt or decrypt the message? (Type 'encrypt' or 'decrypt'): encrypt

Encrypted message: Khoor, Zruog!

Do you want to encrypt or decrypt the message? (Type 'encrypt' or 'decrypt'): decrypt

Decrypted message: Hello, World!

How to Run:

Ensure Python is installed on your system.

Save the script to a file, e.g., caesar_cipher.py.

Run the script using a Python interpreter.

Follow the prompts to input your message, shift value, and desired operation.

