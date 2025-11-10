# Caesar Cipher with File I/O

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) + key - 48) % 10 + 48)
        else:
            result += char
    return result


def decrypt(cipherText, key):
    result = ""
    for char in cipherText:
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) - key - 48) % 10 + 48)
        else:
            result += char
    return result


def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r', encoding='utf-8') as file: 
        plaintext = file.read()
    cipherText = encrypt(plaintext, key)
    with open(output_file, 'w', encoding='utf-8') as file:  
        file.write(cipherText)
    print(f"Encrypted content written to '{output_file}'")


def decrypt_file(input_file, output_file, key):
    with open(input_file, 'r', encoding='utf-8') as file:  
        cipherText = file.read()
    plaintext = decrypt(cipherText, key)
    with open(output_file, 'w', encoding='utf-8') as file:  
        file.write(plaintext)
    print(f"Decrypted content written to '{output_file}'")



def main():
    key = int(input("Enter the key: "))
    while True:
        print("\nMENU: \n1. Encrypt Text\n2. Decrypt Text\n3. Encrypt File\n4. Decrypt File\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            cipherText = encrypt(plaintext, key)
            print(f"CipherText: {cipherText}")
        elif choice == '2':
            cipherText = input("Enter the cipherText: ")
            plaintext = decrypt(cipherText, key)
            print(f"Plaintext: {plaintext}")
        elif choice == '3':
            input_file = input("Enter input file name (with extension): ")
            output_file = input("Enter output file name (with extension): ")
            encrypt_file(input_file, output_file, key)
        elif choice == '4':
            input_file = input("Enter input file name (with extension): ")
            output_file = input("Enter output file name (with extension): ")
            decrypt_file(input_file, output_file, key)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
