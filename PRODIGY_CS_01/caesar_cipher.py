def encrypt_caesar_cipher(plaintext, shift):
    encrypted_message = []
    
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_message.append(encrypted_char)
        else:
            encrypted_message.append(char)
    
    return ''.join(encrypted_message)

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_message = []
    
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift_amount) % 26 + base)
            decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(char)
    
    return ''.join(decrypted_message)

def main():
    print("Caesar Cipher Encryption and Decryption")
    
    # Get user input
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (integer): "))
    operation = input("Do you want to encrypt or decrypt the message? (Type 'encrypt' or 'decrypt'): ").strip().lower()
    
    if operation == 'encrypt':
        encrypted_message = encrypt_caesar_cipher(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif operation == 'decrypt':
        decrypted_message = decrypt_caesar_cipher(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid operation. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
