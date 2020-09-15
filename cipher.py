import diffieHellman
import sys
import os
import random
import string


def genKey(key):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(key))

def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)



# user_input = input("Enter the path of your file: ")
# f = open(user_input,'r')
# x = str(f.readlines())
# print(x)
# f.close()
