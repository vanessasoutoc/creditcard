from src.v1.creditcard.cryptografy import encode, decode


def test_encode_success():
    result = encode('4111111111111111')
    print(result)
    assert result

def test_decode_success():
    key = 'az-C49gKZ_ylgbcl8Ansz44Bds5tdKizh0mDNKkPysQ='
    hash = b'gAAAAABlScDd2Ttk3X4oxcG9qcWZOgEoZyTzE5q6_YpBsI-U3XfVLZMhRUqX1OvX9lCdJGEWWU9jy3OJr_QpaVJbsy6QuhPRZty1N_9zeXxt2u6HA17r3fA='
    result = decode(hash, key)
    assert result == '4111111111111122'
