def is_simple_nubber(x):
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True 