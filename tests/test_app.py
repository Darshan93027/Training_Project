def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(2, 4) == 8

def test_div():
    assert div(10, 2) == 5
