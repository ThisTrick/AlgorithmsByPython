
def count(array: list) -> int:
    ''' Count of numbers from list'''
    _c = 0
    for num in array:
        _c += 1
    return _c    

def sum(array: list) -> float:
    ''' Sum of numbers from list '''
    _s = 0
    for num in array:
        _s += num
    return _s

def product(array: list) -> float:
    ''' Product of numbers from list '''
    _p = 1
    for num in array:
        _p *= num
    return _p

def max(array: list) -> float:
    ''' Max number from list '''
    _m = array[0]
    for num in array:
        _m = num if num > _m else _m
    return _m

def min(array: list) -> float:
    ''' Min number from list'''
    _n = array[0] 
    for num in array:
        _n = num if num < _n else _n
    return _n

def find(array: list, num: float) -> int:
    ''' Find index of number from list '''
    _i = 0
    for _num in array:
        if _num == num:
            return _i
        _i += 1