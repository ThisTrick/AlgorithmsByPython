import Algorithms.OnePass as op
import Testing.Assert as Assert

def start_tests():
    count_array_returned10()
    sum_array_returned314()
    product_array_returned5316256774()
    max_array_returned82()

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

def product_array_returned5316256774():
    #Arrange
    _test_array = get_array()
    _expected = 5316256774
    #Act
    _actual = op.product(_test_array)
    #Assert
    Assert.equal(__name__, product_array_returned5316256774.__name__, _actual, _expected)

def max_array_returned82():
    #Arrange
    _test_array = get_array()
    _expected = 82
    #Act
    _actual = op.max(_test_array)
    #Assert
    Assert.equal(__name__, max_array_returned82.__name__, _actual, _expected)

def min_array_returnedNeg26():
    #Arrange
    _test_array = get_array()
    _expected = -26
    #Act
    _actual = op.min(_test_array)
    #Assert
    Assert.equal(__name__, min_array_returnedNeg26.__name__, _actual, _expected)

def fint_arrayAnd23_returned3():
    #Arrange
    _find = 23
    _test_array = get_array()
    _expected = 3
    #Act
    _actual = op.find(_test_array, _find)
    #Assert
    Assert.equal(__name__, min_array_returnedNeg26.__name__, _actual, _expected)

def fint_arrayAndNeg26_returned9():
    #Arrange
    _find = -26
    _test_array = get_array()
    _expected = 9
    #Act
    _actual = op.find(_test_array, _find)
    #Assert
    Assert.equal(__name__, min_array_returnedNeg26.__name__, _actual, _expected)

