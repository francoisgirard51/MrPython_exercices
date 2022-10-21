# Instructions
# The cards of a game are represented as pairs made up of a string of characters, taken
# from 'heart', 'diamond', 'spade', 'club', and an integer, taken between 2 and 14 (where
# 11 represents the jack, 12 the queen, 13 the king and 14 the ace, which is the most powerful
# card). For example ('club', 11) represents the jack of clubs. The string represents the color
# of the map, the integer represents its height. A card deal is a list containing 5 cards
# (where the order represents the order in which the cards are obtained).
# 
# For example [('club', 11), ('club', 10), ('heart', 3), ('diamond', 11), ('spade', 12)]
# 
# The objective of the exercise is to program functions allowing the identification of certain
# characteristics of distributions, such as the presence of pairs or sequences (defined in the
# following questions) by implementing useful auxiliary functions.
# 
# Define the interleave function which, given a list L of integers ordered from smallest to
# largest and an integer e, constructs the ordered list that contains the same values as L and
# the value e, interleaved at the appropriate place.
def interleave(L:List[int], e:int)->List[int]:
    """Préconditions: len(l)>0 and l is ordered from smallest to largest and e is an integer 
    Returns the ordered list that contains the same values as L and the value e, interleaved
    at the appropriate place.
    """
    Lres: List[int] = []
    pos: int = 0
    while pos<len(L) and L[pos]<=e:
        Lres.append(L[pos])
        pos = pos + 1
    Lres = Lres + [e] + L[pos:]
    return Lres

assert interleave([1, 2, 2, 4], 0) == [0, 1, 2, 2, 4]
assert interleave([1, 2, 2, 4], 1) == [1, 1, 2, 2, 4]
assert interleave([1, 2, 2, 4], 2) == [1, 2, 2, 2, 4]
assert interleave([1, 2, 2, 4], 3) == [1, 2, 2, 3, 4]
assert interleave([1, 2, 2, 4], 4) == [1, 2, 2, 4, 4]
assert interleave([1, 2, 2, 4], 42) == [1, 2, 2, 4, 42]

# Instructions
# Give a definition of the  function which, given a list of integers L, returns
# the list containing the same values as L, ordered from smallest to largest. This
# function just needs to make repeated calls to the interleave function defined in the 
# previous question
def classify(L:List[int])-> List[int]:
    """..."""
    Lres: List[int] = []
    e: int
    for e in L:
        Lres = interleave(Lres, e)
    return Lres

assert classify([4, 2, 1, 2]) == [1, 2, 2, 4]

# Instructions:
# Give a definition of the function got_a_flush which, given a list L of cards of any
# length, returns True if all the cards of L are of the same color and False otherwise.
# By convention, we consider that if the list is empty, it satisfies the property.
def got_a_flush(L:List[Tuple[str, int]]) -> bool:
    """Preconditions: L is a list of cards of any length and c is a color
    c0 is the color of the first card of L and hc0 is the height of the first
    Returns True if all the cards of L are of the same color and False otherwise.
    """
    if len(L) == 0:
        return True
    c0, hc0 = L[0]
    c: str
    hc: int
    for c, hc in L[1:]:
        if c != c0:
            return False
    return True

assert got_a_flush([]) == True
assert got_a_flush([('club', 11), ('club', 10), \
    ('heart', 3),('diamond', 11), ('diamond', 12)]) == False
assert got_a_flush([('club', 11), ('club', 10), \
    ('club', 3), ('club', 4), ('club', 12)]) == True

# Instructions:
# A distribution is said to contain a pair of height h if and only if it contains exactly
# two cards of height h (i.e. 2 such cards but no more). Give a definition of the function
# contains_pair which, given a list of 5 cards D and an integer h, returns True if D
# contains a pair of height h and False otherwise.
def got_a_pair(D:List[Tuple[str, int]], h:int) -> bool:
    """Preconditions: len(D) == 5 and h >= 2 and h <= 14
    returns True if h is the height of a pair in D and False otherwise
    """
    c: str
    hc: int
    nb: int = 0
    for c, hc in D:
        if hc == h:
            nb = nb + 1
        if nb > 2:
            return False
    return nb == 2

assert got_a_pair([('club', 11), ('club', 10), \
    ('heart', 3), ('diamond', 11), ('diamond', 12)], 11) == True
assert got_a_pair([('club', 11), ('club', 10), \
    ('heart', 3), ('diamond', 11), ('diamond', 12)], 3) == False
assert got_a_pair([('club', 11), ('club', 10), \
    ('heart', 3), ('diamond', 11), ('heart', 11)], 11) == False

# Instructions:
# Give a definition of the function extract_col_height which, given a list of 5 cards D and a
# character string col corresponding to one of the four possible colors, returns the list of
# the heights of the cards of this color contained in D.
def extract_col_height(D:List[Tuple[str, int]], col:str) -> List[int]:
    """Préconditions: len(D) == 5 and col is a col == 'heart' or col == 'diamond' or \
    col == 'spade' or col == 'club'
    returns the list of the heights of the cards of this color contained in D.
    """
    c: str
    hc: int
    Lres:List[int] = []
    for c, hc in D:
        if c == col:
            Lres.append(hc)
    return Lres

# Other solution
# def extract_col_height(D:List[Tuple[str, int]], col:str) -> List[int]:
#   return [hc for c, hc in D if c == col]

assert extract_col_height([('club', 11), ('club', 10), \
    ('heart', 3), ('diamond', 11), ('diamond', 12)], 'club') == [11, 10]
assert extract_col_height([('club', 11), ('club', 10), \
    ('heart', 3), ('diamond', 11), ('diamond', 12)], 'heart') == [3]
assert extract_col_height([('club', 11), ('club', 10), \
    ('heart', 3), ('diamond', 11), ('diamond', 12)], 'diamond') == [11, 12]
assert extract_col_height([('club', 11), ('club', 10), \
    ('heart', 3), ('diamond', 11), ('diamond', 12)], 'spade') == []

# Instructions:
# A distribution is said to contain a sequence of height h if and only if it contains five
# consecutive cards of the same suit, the highest of which has the value h. Give a definition
# of the sequence function which, given a list of 5 cards D and an integer h, returns True if
# D contains a sequence of height h and False otherwise.
def got_a_straight_flush(D:List[Tuple[str, int]], h:int) -> bool:
    """Preconditions: len(D) == 5 and h >= 2 and h <= 14
    Returns True if D contains a sequence of height h and False otherwise.
    """
    if got_a_flush(D):
        list_height:List[int] = [hauteur for (_, hauteur)in D]
        height_classified:List[int] = classify(list_height)
        if height_classified[-1] != h:
            return False
        pos: int
        for pos in range(0, 4):
            if height_classified[pos + 1] != height_classified[pos] + 1:
                return False
        return True
    return False

assert got_a_straight_flush([('heart', 11), ('club', 10), \
    ('club', 9), ('spade', 8), ('club', 12)], 12) == False
assert got_a_straight_flush([('club', 11), ('club', 10), \
    ('club', 3), ('club', 4), ('club', 12)], 12) == False
assert got_a_straight_flush([('club', 11), ('club', 10), \
    ('club', 9), ('club', 8), ('club', 12)], 8) == False
assert got_a_straight_flush([('club', 11), ('club', 10), \
    ('club', 9), ('club', 8), ('club', 12)], 12) == True
