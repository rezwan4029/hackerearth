from Crypto.Cipher import AES


def decryption():
    with open('encrypted_key.txt', 'r') as f:
        encryptedString = f.read()
    decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    plain_text = decryption_suite.decrypt(encryptedString)
    #print plain_text
    return plain_text