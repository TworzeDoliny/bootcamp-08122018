from mathematica.algebra import matrices

def test_add_matrices():
    a = [[1, 2], [10, 10]]
    b = [[2, 3], [5, 6]]
    assert a == [[11, 12]]
    assert b == [[7, 9]]

