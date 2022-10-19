# Instructions:
# Give a definition of the function prop_even_digits which,
# given a positive or zero integer n, returns the proportion
# of even digits that n contains, i.e. the quotient between
# its number of even digits and its total number of digits.

def prop_even_digits(n:int)->float:
    '''Preconditions: n is a positive or zero integer
    Returns the proportion of even digits of n, i.e. the
    quotient between the number of even digits of n and
    the total number of digits of n.
    '''

    p:int = n
    if p == 0:
        return 1
    else:
        nb: int = 0
        nb_even: int = 0
        while p != 0:
            nb = nb + 1
            if p % 2 == 0:
                nb_even = nb_even + 1
            p = p // 10
        return nb_even / nb
    
assert prop_even_digits(42) == 1.0
assert prop_even_digits(5317) == 0.0
assert prop_even_digits(5417) == 0.25
assert prop_even_digits(1234567890) == 0.5
assert prop_even_digits(0) == 1

# Instructions:
# We choose to say that a number has an even tendency
# if the majority of its digits are even. Give a definition
# of the trend_pair function which, given a positive or zero
# integer n, returns True if n has an even trend and False
# otherwise.

def evenly_trended(n:int)->bool:
    '''Preconditions: n is a positive or zero integer
    returns True if n has an even trend and False otherwise.
    '''
    
    return prop_even_digits(n) >= 0.5

assert evenly_trended(42) == True
assert evenly_trended(5317) == False
assert evenly_trended(5347) == False
assert evenly_trended(1234567890) == True
assert evenly_trended(0) == True

# Instructions:
# Give a definition of the statistics function which, given
# a positive or zero integer n, returns returns the number
# of integers between 0 and n (inclusive) that are evenly tended.

def statistics(n:int)->int:
    '''Preconditions: n is a positive or zero integer
    returns the number of integers between 0 and n (inclusive)
    that are evenly tended.
    '''
    nb: int = 0
    i: int
    for i in range(n+1):
        if evenly_trended(i):
            nb = nb + 1
    return nb

assert statistics(0) == 1
assert statistics(10) == 6
assert statistics(100) == 71
assert statistics(1000) == 496