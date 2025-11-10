
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Padding (PKCS7)
def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# AES Encryption
def encrypt_aes(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode()))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# AES Decryption
def decrypt_aes(iv, ciphertext, key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ciphertext)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct)).decode('utf-8')
    return pt

# Example usage
key = get_random_bytes(16)  # 128-bit key
message = "This is a secret message"

print(f"Original Message: {message}")

iv, ciphertext = encrypt_aes(message, key)
print(f"Encrypted (Base64): {ciphertext}")

decrypted_msg = decrypt_aes(iv, ciphertext, key)
print(f"Decrypted Message: {decrypted_msg}")
