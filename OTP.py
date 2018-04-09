import string
import random

class OTP(object):
    def __init__(self, message):
        self.msglen = len(message)
        self.message = "".join([str(ord(char)) for char in list(message)])

    def encrypt(self, key):
        cipher = int(self.message) ^ key
        return cipher

    def decrypt(self, key):
        plaintext = int(self.message) ^ key
        return plaintext

    def generate(self):
        key = [str(ord(random.choice(string.ascii_letters + string.digits))) for i in range(0, len(self.message))]
        return "".join(key)[:self.msglen]

