def add_numbers(x, y):
    return x + y
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, 5) == 0