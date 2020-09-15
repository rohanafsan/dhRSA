from cipher import genKey, encrypt, decrypt
from Crypto.Util import number
import diffieHellman
import sys
import os
import random
import string

if diffieHellman.sharedClient != diffieHellman.sharedServer:
    raise Exception("Sorry, Diffie-Hellman key exchange has failed")

diffieKey = genKey(diffieHellman.sharedClient)

def genE():
    e = random.randint(1, phi)
    coprime = gcd(e, phi)
    while coprime != 1:
        e = random.randint(1, phi)
        coprime = gcd(e, phi)
    return e

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcdExtended(a, b):
    if a == 0 :
        return (b,0,1)
    gcd,x1,y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return (gcd,x,y)


p = number.getPrime(5)
q = number.getPrime(5)
n = p * q
phi = (p-1) * (q-1)
e = genE()
d = gcdExtended(e,phi)[1]
d = d % phi
if(d < 0):
    d += phi

cmd = str(input("Do you want to encrypt or decrypt: "))

if cmd == "encrypt":
    encryptLines = []
    user_input = input("Enter the path of your file to encrypt: ")
    f = open(user_input,'r')
    lines = f.readlines()
    for line in lines:
        encryptLines.append(str(line))
    f.close()


    for lines in encryptLines:
        encodeText = encrypt(diffieKey, lines)
        print(encodeText)
        # ordc = [ord(c) for c in lines]
        ordc = [ord(c) for c in encodeText]
        print(ordc)
        for i in range(0, len(ordc)):
            ordc[i] = pow(ordc[i], e) % n

        res = str(" ".join(map(str, ordc)))
        f = open("encrypted.txt", "a")
        f.write(res)
        f.write("\n")
    f.write(str(diffieKey))
    f.write("\n")
    f.write(str(d))
    f.write("\n")
    f.write(str(n))

elif cmd == "decrypt":
    user_input = input("Enter the path of your file: ")
    f = open(user_input,'r')
    decryptLines = []
    lines = f.readlines()
    for line in range(0, len(lines)-3):
        decryptLines.append(list(map(int, lines[line].split())))
    f.close()

    diffieKey = str(lines[-3])
    d = int(lines[-2])
    n = int(lines[-1])
    for lines in decryptLines:
        ordc = lines
        #Decryption
        decrc = [0] * len(ordc)

        for i in range(0, len(ordc)):
            decrc[i] = pow(ordc[i], d) % n
        print(decrc)
        charc = [chr(c) for c in decrc]
        print(charc)
        res = str("".join(charc))
        print(res)
        decodeText =  decrypt(diffieKey, res)
        print(decodeText)
        f = open("decrypted.txt", "a")
        f.write(decodeText)
else:
    raise Exception("Sorry, incorrect command")
