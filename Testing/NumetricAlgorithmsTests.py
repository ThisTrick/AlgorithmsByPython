import Testing.Assert as Assert
import Algorithms.NumetricAlgorithms as na

def start_tests():
    is_simple_nubber_17_returnedTrue()
    is_simple_nubber_35_returnedFalse()
    factorize_number_1024_returned2x10()

def is_simple_nubber_17_returnedTrue():
    #Arrange
    _expected = True
    #Act
    _actual = na.is_simple_nubber(17)
    #Assert
    Assert.equal(__name__, is_simple_nubber_17_returnedTrue.__name__, _actual, _expected)

def is_simple_nubber_35_returnedFalse():
    #Arrange
    _expected = False
    #Act
    _actual = na.is_simple_nubber(35)
    #Assert
    Assert.equal(__name__, is_simple_nubber_17_returnedTrue.__name__, _actual, _expected)

def factorize_number_1024_returned2x10():
    #Arrange
    _expected = [2] * 10
    #Act
    _actual = na.factorize_number(1024)
    #Assert
    Assert.arrays_equal(__name__, factorize_number_1024_returned2x10.__name__, _actual, _expected)

