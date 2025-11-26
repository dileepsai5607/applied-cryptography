# ----------------------------------------------------
# ECC Implementation with User Input (secp256k1)
# ----------------------------------------------------

import secrets

# secp256k1 parameters
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A = 0
B = 7

Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (Gx, Gy)

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


# -----------------------------------------------
# Modular inverse
# -----------------------------------------------
def modinv(a, n=P):
    return pow(a, n - 2, n)


# -----------------------------------------------
# Point addition
# -----------------------------------------------
def point_add(P1, P2):
    if P1 is None:
        return P2
    if P2 is None:
        return P1

    x1, y1 = P1
    x2, y2 = P2

    if x1 == x2 and y1 != y2:
        return None

    if P1 == P2:  # doubling
        s = (3 * x1 * x1) * modinv(2 * y1)
    else:
        s = (y2 - y1) * modinv(x2 - x1)

    s %= P
    x3 = (s * s - x1 - x2) % P
    y3 = (s * (x1 - x3) - y1) % P

    return (x3, y3)


# -----------------------------------------------
# Scalar multiplication (double-and-add)
# -----------------------------------------------
def scalar_mult(k, P):
    result = None
    addend = P

    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1

    return result


# -----------------------------------------------
# ECDH Shared Secret
# -----------------------------------------------
def ecdh(priv_key, pub_key):
    point = scalar_mult(priv_key, pub_key)
    return point[0]  # x-coordinate as secret


# -----------------------------------------------
# Main Program (User Input)
# -----------------------------------------------
print("===== Elliptic Curve Cryptography (ECC) Demo =====")

# User private key inputs
a_priv = int(input("Enter Alice's private key: "))
b_priv = int(input("Enter Bob's private key: "))

# Public key generation
a_pub = scalar_mult(a_priv, G)
b_pub = scalar_mult(b_priv, G)

print("\n=== Generated Public Keys ===")
print("Alice Public Key:", a_pub)
print("Bob Public Key  :", b_pub)

# Shared secrets
a_secret = ecdh(a_priv, b_pub)
b_secret = ecdh(b_priv, a_pub)

print("\n=== ECDH Shared Secret ===")
print("Alice's Secret:", a_secret)
print("Bob's Secret  :", b_secret)

# Verify match
print("\nSecrets Match? ->", a_secret == b_secret)
