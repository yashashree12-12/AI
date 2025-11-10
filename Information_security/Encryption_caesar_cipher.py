# Caesar Cipher
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


def main():
    key = int(input("Enter the key: "))
    while True:
        print("\nMENU: \n1. Encrypt\n2. Decrypt\n3. Exit")
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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
