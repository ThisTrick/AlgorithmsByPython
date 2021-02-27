import Testing.Assert as Assert
import Algorithms.NumetricAlgorithms as na

def start_tests():
    is_simple_nubber_17_returnedTrue()
    is_simple_nubber_35_returnedFalse()

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

