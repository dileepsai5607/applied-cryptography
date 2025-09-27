import random
from math import gcd

# Function to check if number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a random prime number
def generate_prime(start=50, end=200):
    while True:
        prime = random.randint(start, end)
        if is_prime(prime):
            return prime

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Key Generation
p = generate_prime()
q = generate_prime()
while q == p:
    q = generate_prime()

n = p * q
phi = (p - 1) * (q - 1)

# Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = random.randrange(2, phi)
while gcd(e, phi) != 1:
    e = random.randrange(2, phi)

# Compute d (modular inverse of e)
d = mod_inverse(e, phi)

# Public and Private Keys
public_key = (e, n)
private_key = (d, n)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Encryption function
def encrypt(message, pub_key):
    e, n = pub_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

# Decryption function
def decrypt(ciphertext, priv_key):
    d, n = priv_key
    message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return message

# --- USER INPUT ---
message = input("Enter a message to encrypt: ")

ciphertext = encrypt(message, public_key)
print("Encrypted message:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted message:", decrypted_message)
