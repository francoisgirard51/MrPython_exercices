# Instruction:
# Give a definition of the function second_smallest which, given three numbers
# two by two distinct, returns the second smallest of the three.

def second_smallest(a:float, b:float, c:float)->float:
    '''Preconditions: a, b, c are three numbers two by two distinct
    Postconditions: returns the second smallest of the three'''
    
    if a < b:
        if a < c:
            if b < c:
                return b
            else:
                return c
        else:
            return a
    else:
        if b < c:
            if a < c:
                return a
            else:
                return c
        else:
            return b

assert second_smallest(12.3, 14.2, -8) == 12.3
assert second_smallest(12.3, 14.2, 18) == 14.2
assert second_smallest(-1, 0, 1) == 0
assert second_smallest(-9.35, 88, -9.34) == -9.34 