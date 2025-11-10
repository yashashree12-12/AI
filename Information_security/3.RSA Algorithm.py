import math
from sympy import mod_inverse

# Step 1: Choose two prime numbers
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))

# Step 2: Calculate n
n = p * q
print("n =", n)

# Step 3: Compute Euler’s Totient function
phi = (p - 1) * (q - 1)

# Step 4: Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1
print("e =", e)

# Step 5: Calculate d, modular multiplicative inverse of e mod phi
d = mod_inverse(e, phi)
print("d =", d)

# Step 6: Display public and private keys
print(f"Public key: ({e}, {n})")
print(f"Private key: ({d}, {n})")

# Step 7: Input message (as integer)
msg = int(input("Enter the message (as a number): "))
print(f"Original message: {msg}")

# Step 8: Encryption
C = pow(msg, e, n)
print(f"Encrypted message: {C}")

# Step 9: Decryption
M = pow(C, d, n)
print(f"Decrypted message: {M}")

# Enter a prime number p: 11
# Enter a prime number q: 13
# n = 143
# e = 7
# d = 103
# Public key: (7, 143)
# Private key: (103, 143)
# Enter the message (as a number): 9
# Original message: 9
# Encrypted message: 48
# Decrypted message: 9
