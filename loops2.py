# Instructions:
# We consider the function f defined by f:Z -> Z
#   n -> -((n^2)/2)-2*n+1 if n is even and n belongs to [0, 20[
#   n -> (n^2)-n+2 if n is odd and n belongs to [-10, 0[
#   n -> 2*n-5 otherwise
# and the serie defined by induction by for a given value a
# u_0 = a
# u_n+1 = f(u_n) if n >= 0
# Give a definition of the function f which, given an integer n, returns the value of f(n).

def f(n: int) -> int:
    '''Preconditions: n is an integer
    returns the value of f(n)
    '''
    if n % 2 == 0 and n >= 0 and n < 20:
        return -n ** 2//2 - 2 * n + 1
    elif n % 2 == 1 and n >= -10 and n < 0:
        return (n**2)-n+2
    else:
        return 2*n-5
    
assert f(0) == 1
assert f(5) == 5
assert f(20) == 35
assert f(-8) == -21

# Instructions:
# Give a definition of the serie function which, given an integer a and a positive
# integer n, returns the value of u_n defined by equation (2) with u0 = a.

def serie(u0: int, n: int) -> int:
    '''Preconditions: n>=0 and u0 is an integer
    Returns the value of u_n defined by equation (2) with u0 = a
    '''
    u: int = u0
    i: int
    for i in range(1, n+1):
        u = f(u)
    return u

assert serie(5, 10) == 5
assert serie(0, 1) == 1
assert serie(2, 3) == 59

# Instructions:
# Give a definition of the function index_max which, given an integer a and a
# positive integer n, returns the index of the greatest value among the terms
# u_0, u_1, . . . , one for the sequence defined by equation (2) with u0 = a.
# In the event of a tie, the smallest of the indices corresponding to the
# maximum must be returned.

def index_max(u0:int, n: int) -> int:
    '''Preconditions: n>=0 and a is an integer
    Returns the index of the greatest value among the terms u_0, u_1, . . . ,
    one for the sequence defined by equation (2) with u0 = a.
    In the event of a tie, the smallest of the indices corresponding to the
    maximum must be returned.
    '''
    u: int = u0
    highest: int = u0
    pos_highest: int = 0
    i: int
    for i in range(1, n+1):
        u = f(u)
        if u>highest:
            highest = u
            pos_highest = i
    return pos_highest

assert index_max(5, 20) == 0
assert index_max(0, 10) == 3
assert index_max(2, 10) == 10

# Instructions:
# Give the loop simulation array for indice_max(0, 5).
# 
# |-----------------------------------------|
# | Round | i |  u  | highest | pos_highest |
# |-------|---|-----|---------|-------------|
# | 1     | 1 | 1   | 1       | 1           |
# |-------|---|-----|---------|-------------|
# | 2     | 2 | -3  | 1       | 1           |
# |-------|---|-----|---------|-------------|
# | 3     | 3 | 14  | 14      | 3           |
# |-------|---|-----|---------|-------------|
# | 4     | 4 | -125| 14      | 3           |
# |-------|---|-----|---------|-------------|
# | 5     | 5 | -255| 14      | 3           |
# |-----------------------------------------|

# Instructions:
# Propose a variant as well as a loop invariant for the indice_max function
# that you have defined, and complete the previous loop simulation table to verify them.
# 
# Variant: n-i
# Invariant pos_highest = arg max_(l=1..i) * u_l
# 
# |--------------------------------------------------------------------------------------------|
# | Round | i |  u  | highest | pos_highest | n - i |   pos_highest = arg max_(l=1..i) * u_l   |
# |-------|---|-----|---------|-------------|-------|------------------------------------------|
# | 1     | 1 | 1   | 1       | 1           | 4     | 1 = arg max{1} (True)                    |
# |-------|---|-----|---------|-------------|-------|------------------------------------------|
# | 2     | 2 | 1   | 1       | 1           | 3     | 1 = arg max{1, 1} (True)                 |
# |-------|---|-----|---------|-------------|-------|------------------------------------------|
# | 3     | 3 | -3  | 14      | 3           | 2     | 3 = arg max{1, 1, -3} (True)             |
# |-------|---|-----|---------|-------------|-------|------------------------------------------|
# | 4     | 4 | -125| 14      | 3           | 1     | 3 = arg max{1, 1, -3, -125} (True)       |
# |-------|---|-----|---------|-------------|-------|------------------------------------------|
# | 5     | 5 | -255| 14      | 3           | 0     | 3 = arg max{1, 1, -3, -125, -255} (True) |
# |--------------------------------------------------------------------------------------------|
# 
# At the exit of the for loop, the variable i is worth n, therefore n − i = 0, therefore the
# function terminates. Moreover, the variable pos_plus_grand is therefore equal to arg maxl=1..n ul,
# which corresponds well to the desired result. Also, the function is correct.
