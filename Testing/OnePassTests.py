import Algorithms.OnePass as op
import Testing.Assert as Assert

def start_tests():
    count_array_returned10()
    sum_array_returned314()

def get_array():
    return [12, 54, 82, 23, 58, 82, 1, 3, 25, -26]

def count_array_returned10():
    # Arrange
    _test_array = get_array()
    _expected = 10
    # Act
    _actual = op.count(_test_array)
    #Assert
    Assert.equal(__name__, count_array_returned10.__name__, _actual, _expected) 

def sum_array_returned314():
    #Arrange
    _test_array = get_array()
    _expected = 314
    #Act
    _actual = op.sum(_test_array)
    #Assert
    Assert.equal(__name__, sum_array_returned314.__name__, _actual, _expected)

