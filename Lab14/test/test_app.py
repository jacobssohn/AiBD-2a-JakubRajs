import pytest
from app import *
import numpy as np
import random

def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata = ["I think today will be a great day","I think this will turn out great"]
@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

testdata = [[[random.randint(1, 20) for _ in range(5)] for _ in range(5)] for _ in range(100)]
@pytest.mark.parametrize('matrix', testdata)
def test_isSquare(matrix):
    dimensions = np.shape(matrix)
    assert isSquare(matrix) == (dimensions[0] == dimensions[1])

@pytest.mark.parametrize('matrix', testdata)
def test_determinant(matrix):

    assert np.around(determinant(matrix), decimals=5) == np.around(np.linalg.det(matrix), decimals=5)
