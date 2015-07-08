from Crypto.Cipher import AES
#base64 is used for encoding. dont confuse encoding with encryption#
#encryption is used for disguising data
#encoding is used for putting data in a specific format
import base64
# os is for urandom, which is an accepted producer of randomness that
# is suitable for cryptology.
import os

f = open('encrypted_key.txt', 'w')


def encryption(privateInfo):

    encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    cipher_text = encryption_suite.encrypt(privateInfo)
    f.write(cipher_text)
    print 'Done !'

"""
    Ex:
        DJANGO_SETTINGS_MODULE=newspapers.settings python -m manage shell

        >> from encrypt_decrypt.encrypt import encryption
        >> newscred_access_key = '?'
        >> encryption(newscred_access_key)

"""