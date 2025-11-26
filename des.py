from pyDes import des, ECB, PAD_PKCS5

# ------------------------------------
# DES Encryption / Decryption Program
# ------------------------------------

print("===== DES Encryption & Decryption =====")

# User inputs
plaintext = input("Enter plaintext: ")
key = input("Enter 8-character key: ")

# Key must be exactly 8 bytes
if len(key) != 8:
    print("Error: Key must be 8 characters (64 bits).")
    exit()

# Create DES object
cipher = des(key, ECB, padmode=PAD_PKCS5)

# Encryption
encrypted = cipher.encrypt(plaintext)
print("\nEncrypted (ciphertext bytes):", encrypted)
print("Encrypted (hex):", encrypted.hex())

# Decryption
decrypted = cipher.decrypt(encrypted)
print("Decrypted text:", decrypted.decode())
