from src.v1.creditcard.cryptografy import encode, decode


def test_encode_success():
    result = encode('4111111111111111')
    assert result

def test_decode_success():
    hash_number = encode('4111111111111111').decode('utf-8')
    result = decode(hash_number)
    assert result == '4111111111111111'

def test_decode_fail():
    hash_value = ""
    dec = decode(hash_value)
    assert not dec
