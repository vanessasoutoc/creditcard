import cryptography.fernet


def encode(number):
    key = cryptography.fernet.Fernet.generate_key()
    f = cryptography.fernet.Fernet(key)
    return {'credit_card': f.encrypt(number.encode('ascii')), 'key': key}

def decode(ciphertext, key):
    f = cryptography.fernet.Fernet(key)
    number = f.decrypt(ciphertext).decode('ascii')
    return number

