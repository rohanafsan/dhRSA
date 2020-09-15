import diffieHellmanSetup
import secrets
secretsGenerator = secrets.SystemRandom()

# Sets up Public keys
p = diffieHellmanSetup.p
n = diffieHellmanSetup.n

# Client secret key
a = secretsGenerator.randint(3,10000)
A = pow(n, a) % p


# Server secret Key
b = secretsGenerator.randint(3,10000)
B = pow(n, b) % p


# Shared key to be used in blowFish algorithm
sharedClient = (B ** a) % p
sharedServer = (A ** b) % p
