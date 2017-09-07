from RLE import encode,decode
from pytest import raises

def test_encode():
    assert encode('kkkkkbbbb') == '5k4b'

def test_encode_empty():
    assert encode('') == ''

def test_encode_space():
    assert encode(' ') == '1 '

def test_encode2():
    assert encode('a') == '1a'

def test_encode_signs():
    assert encode('.?') == '1.1?'

def test_encode_newline():
    assert encode('\n') == '1\n'

def test_encode_caps():
    assert encode('AAAA') == '4A'

def test_encode_danish():
    assert encode('æøå') == '1æ1ø1å'

def test_encode_numbers():
    assert encode('11') == '21'

def test_encode_emoji():
    assert encode('😇') == '1😇'
    assert encode('😇😇😇😇😇') == '5😇'

#def test_exeption():
#    raises(encode(111),TypeError)

def test_decode():
    assert decode('4k') == 'kkkk'
    assert decode('4k3b') == 'kkkkbbb'
    assert decode('4😇') == '😇😇😇😇'
    assert decode('10æ') == 'ææææææææææ'

def test_decode_empty():
    assert decode('') == ''

def test_decode_error():
    assert decode('1') == ''
#    assert decode('4k-----10æ') == ''
