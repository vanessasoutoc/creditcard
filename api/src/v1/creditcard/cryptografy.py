import cryptography.fernet

key = 'w0qnrvVVlxQMDar0OMsK26AYefaMCzK24-N8ee7zA2k='

def encode(number: str):
    f = cryptography.fernet.Fernet(key)
    return {'credit_card': f.encrypt(number.encode('ascii')), 'key': key}

def decode(number: str):
    try:
        f = cryptography.fernet.Fernet(key)
        number = f.decrypt(bytes(number, encoding="raw_unicode_escape")).decode('ascii')
        return number
    except Exception as error:
        print(error)

