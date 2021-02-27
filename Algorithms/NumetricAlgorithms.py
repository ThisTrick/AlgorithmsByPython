def is_simple_nubber(x):
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True 

def factorize_number(x):
    divisor = 2
    array = []
    while x > 1:
        if x % divisor == 0:
            array.append(divisor)
            x //= divisor
        else : divisor += 1
    return array