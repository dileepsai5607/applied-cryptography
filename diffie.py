def power(base, exponent, modulus): 

return pow(base, exponent, modulus) 

 

print("=== Diffie–Hellman Key Exchange ===") 

 

# Step 1: Publicly known parameters (prime number and primitive root) 

P = int(input("Enter a large prime number (P): ")) 

G = int(input("Enter a primitive root of P (G): ")) 

 

print(f"\nPublicly known values:\n P = {P}\n G = {G}") 

 

# Step 2: Each user chooses a private key (kept secret) 

a = int(input("\nUser A, enter your private key (a): ")) 

b = int(input("User B, enter your private key (b): ")) 

 

# Step 3: Generate public keys 

x = power(G, a, P) # A's public key 

y = power(G, b, P) # B's public key 

 

print(f"\nUser A's Public Key (x) = {x}") 

print(f"User B's Public Key (y) = {y}") 

 

# Step 4: Exchange public keys and compute shared secret 

ka = power(y, a, P) # Secret key for A 

kb = power(x, b, P) # Secret key for B 

 

print("\n=== Secret Keys Computed ===") 

print(f"Secret Key (computed by A) = {ka}") 

print(f"Secret Key (computed by B) = {kb}") 

 

# Verify that both secret keys are the same 

if ka == kb: 

print("\n✅ Key exchange successful! Shared secret key =", ka) 

else: 

print("\n❌ Key exchange failed! Keys do not match.") 
