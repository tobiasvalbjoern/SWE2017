﻿from RLE import encode, decode
from pytest import raises

#For the hypothesis
from hypothesis import given
from hypothesis.strategies import text


def test_encode():
    assert encode('kkkkkbbbb') == [(5,'k'),(4,'b')]
    assert encode('111k') == [(3,'1'),(1,'k')]

def test_encode_empty():
    assert encode('') == ''

def test_encode_space():
    assert encode(' ') == [(1,' ')]

def test_encode2():
    assert encode('a') == [(1,'a')]

def test_encode_signs():
    assert encode('.?') == [(1,'.'),(1,'?')]

def test_encode_newline():
    assert encode('\n') == [(1,'\n')]

def test_encode_caps():
    assert encode('AAAA') == [(4,'A')]

def test_encode_danish():
    assert encode('æøå') == [(1,'æ'),(1,'ø'),(1,'å')]

def test_encode_numbers():
    assert encode('11') == [(2,'1')]

def test_encode_emoji():
    assert encode('😇') == [(1,'😇')]
    assert encode('😇😇😇😇😇') == [(5,'😇')]

def test_decode():
    assert decode([(5,'k'),(4,'b')]) == 'kkkkkbbbb'
    assert decode([(5,'K')]) == 'KKKKK'
    assert decode([(1,'\n')]) == '\n'	
    assert decode([(1,' ')]) == ' '	
    assert decode([(1,'😇')]) == '😇'
    assert decode([(1,'1')]) == '1'	
    assert decode([(5,'😇')]) == '😇😇😇😇😇'
    assert decode([(10,'æ')]) == 'ææææææææææ'

def test_decode_empty():
    assert decode('') == ''

#For hypothesis
@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s