import Algorithms.OnePass as op

def get_array():
    return [12, 54, 82, 23, 58, 82, 1, 3, 25, -26]

def count_test_returned10():
    # Arrange
    _test_array = get_array()
    _expected = 10
    # Act
    _actual = op.count(_test_array)
    #Assert
    return _actual == _expected
