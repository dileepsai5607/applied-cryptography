import random
from math import gcd
import hashlib

# --- Prime number functions ---
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(start=100, end=300):
    while True:
        prime = random.randint(start, end)
        if is_prime(prime):
            return prime

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# --- Key Generation ---
p = generate_prime()
q = generate_prime()
while q == p:
    q = generate_prime()

n = p * q
phi = (p - 1) * (q - 1)

e = random.randrange(2, phi)
while gcd(e, phi) != 1:
    e = random.randrange(2, phi)

d = mod_inverse(e, phi)

public_key = (e, n)
private_key = (d, n)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# --- Signing Function ---
def sign(message, priv_key):
    d, n = priv_key
    hash_value = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    signature = pow(hash_value, d, n)
    return signature

# --- Verification Function ---
def verify(message, signature, pub_key):
    e, n = pub_key
    hash_value = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    hash_from_signature = pow(signature, e, n)
    return hash_value == hash_from_signature

# --- User Input ---
message = input("Enter the message to sign: ")

signature = sign(message, private_key)
print("\nSignature:", signature)

is_valid = verify(message, signature, public_key)
print("Is the signature valid?", is_valid)
