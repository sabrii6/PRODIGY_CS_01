def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            # Determine the character's position in the alphabet
            char_code = ord(char.lower()) - ord('a')
            # Apply the shift
            shifted_code = (char_code + shift) % 26
            # Convert back to a letter
            shifted_char = chr(shifted_code + ord('a'))
            # Preserve the case
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char  # Preserve non-alphabetic characters
    return result


def encrypt_message(message, shift):
    return caesar_cipher(message, shift)


def decrypt_message(encrypted_message, shift):
    # To decrypt, just shift in the opposite direction
    return caesar_cipher(encrypted_message, -shift)


def main():
    print("Welcome to Cipher Encrypt/Decrypt Tool!!!")
    while True:
        print("\n1. Encrypt Message\n2. Decrypt Message\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift (a number between 1 and 25): "))
            encrypted_message = encrypt_message(message, shift)
            print("Encrypted Message:", encrypted_message)
            perform_another_operation = input("Do you want to perform another operation? (yes/no): ")
            if perform_another_operation.lower() != 'yes':
                break

        elif choice == '2':
            encrypted_message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift used for encryption: "))
            decrypted_message = decrypt_message(encrypted_message, shift)
            print("Decrypted Message:", decrypted_message)
            perform_another_operation = input("Do you want to perform another operation? (yes/no): ")
            if perform_another_operation.lower() != 'yes':
                break

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
