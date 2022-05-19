import math


# filter


def test_filter():
    assert list(filter(lambda x: x[1] == 'e', ['Leo', 'lao', 'luo', 'lio', 'leo'])) == ['Leo', 'leo']
    assert list(filter(lambda x: x == 'leo', ['Leo', 'lao', 'luo', 'lio', 'leo'])) == ['leo']
    mixed = ['мак', 'рис', 'мак', 'мак', 'просо', 'макдоналдс', 'пшено', 'горох', 'ячмень', 'мак']
    assert list(filter(lambda x: x == 'мак', mixed)) == ['мак', 'мак', 'мак', 'мак']
    numbers_tuple = (range(-10, 10))
    assert list(filter(lambda x: x % 2 == 0, numbers_tuple)) == [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]
    assert list(filter(lambda x: x % 3 == 0, numbers_tuple)) == [-9, -6, -3, 0, 3, 6, 9]
    assert tuple(filter(lambda x: x >= 0, numbers_tuple)) == (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert tuple(filter(lambda x: x < 0, numbers_tuple)) == (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1)


def test_map():
    assert list(map(lambda x: x * 2, range(4))) == [0, 2, 4, 6]
    assert len(list(map(lambda x: x * 2, range(4)))) == 4
    assert list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])) == [1, 1, 1]


def test_sorted():
    assert sorted([1, 2, 3], reverse=True) == [3, 2, 1]
    assert sorted(['3', '2', '1'], key=int) == ['1', '2', '3']
    assert sorted('Hello World!') == [' ', '!', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']


def test_pi():
    assert math.pi == 3.141592653589793


def test_math_sqrt():
    assert math.sqrt(256) == 16.0
    assert math.sqrt(256) == 16
    assert isinstance(math.sqrt(9), float)


def test_math_pow():
    assert math.pow(2, 8) == 256
    assert math.pow(2, 4) % 2 == 0
    assert math.pow(5, 0) == 1
    assert math.pow(10, 3) == 1000
    assert math.pow(10, -3) == 10 ** -3


def test_math_hypot():
    assert math.hypot(3, 4) == 5.0
    assert math.hypot(8, 6) == 10.
    assert math.hypot(-2, 0) == 2


def test_math_sqrt_and_pow():
    """
    От себя добавил:
    """
    for i in range(255):
        assert math.sqrt(math.pow(i, 2)) == i
