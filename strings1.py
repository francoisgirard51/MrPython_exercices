# Instructions:
# Give a definition of the alternate function which, given three character
# strings of the same length, returns the character string obtained by taking
# one character from each of the three in turn.

def alternate(s1:str, s2:str, s3:str)->str:
    '''Preconditions: s1, s2 and s3 are character strings of the same length
    returns the character string obtained by taking one character from each
    of the three in turn.
    '''
    
    s: str = ""
    i: int
    for i in range(len(s1)):
        s = s + s1[i] + s2[i] + s3[i]
    return s

assert alternate('ABCDE', 'abcde', 'VWXYZ') == 'AaVBbWCcXDdYEeZ'
assert alternate('a', 'b', 'c') == 'abc'
assert alternate('', '', '') == ''

# ---
# Instructions:
# Give a definition of the extract function which, given a string of characters s and
# two characters car1 and car2, returns the portion of the string s between the first
# occurrence of car1 (excluded) and the first occurrence of car2 which follows 
# (excluded). If char1 does not appear, the returned string must be empty; if char1
# appears but char2 does not, the returned string must go to the end of s.

def extract(s:str, char1:str, char2:str)->str:
    '''Preconditions: s is a character string, char1 and char2 are characters
    returns the portion of the string s between the first occurrence of car1 (excluded)
    and the first occurrence of car2 which follows (excluded). If char1 does not appear,
    the returned string must be empty; if char1 appears but char2 does not, the
    returned string must go to the end of s.
    '''
    
    i: int = 0
    while i < len(s) and s[i] != char1:
        i = i + 1
    if i == len(s):
        return ''
    else:
        j: int = i + 1
        while j < len(s) and s[j] != char2:
            j = j + 1
        return s[i+1:j]
        
assert extract('abracadabra', 'b', 'd') == 'raca'
assert extract('abracadabra', 'c', 'b') == 'ada'
assert extract('abracadabra', 'a', 'b') == ''
assert extract('abracadabra', 'a', 'a') == 'br'
assert extract('abracadabra', 'a', 'e') == 'bracadabra'
assert extract('abracadabra', 'e', 'a') == ''

# ---
# Instructions:
# Give a definition of the function remove_if which, given a string of characters s,
# a character char and a strictly positive integer n, returns the string obtained from s
# by removing the blocks containing n occurrences of char in a row. When the car character
# appears exactly n times in a row, this whole block must be deleted. When it appears a
# different number of times in a row, the block must be kept.

def remove_if(s:str, char:str, n:int)->str:
    '''Preconditions: s is a character string, char is a character, n is a strictly positive integer
    returns the string obtained from s by removing the blocks containing n occurrences of char in a row.
    '''
    i: int = 0
    p: str = s
    while i < len(p):
        j: int = i
        while j < len(p) and p[j] == char:
            j = j + 1
        if j - i == n:
            p = p[:i] + p[j:]
        else:
            i = j + 1
    return p

assert remove_if('creee', 'e', 3) == 'cr'
assert remove_if('creee','e', 2) == 'creee'
assert remove_if('libellule','l', 2) == 'libeule'
assert remove_if('libellule','l', 1) == 'ibellue'
assert remove_if('papillon','p', 1) == 'aillon'
assert remove_if('papillon','l', 2) == 'papion'
assert remove_if('papillon','l', 1) == 'papillon'
