# Instructions:
# Give a definition of the initial function which, given a string corresponding
# to the word to find, returns the string of the same size containing only "*".

def initialise(word: str) -> str:
    '''Preconditions: word is a string and does not contain "*"
    returns a string of the same size as word, containing only "*"
    '''
    return "*" * len(word)

assert initialise("abracadabra") == "***********"
assert initialise("bonjour") == "*******"
assert initialise("a") == "*"

# ---
# Instructions:
# We then want to be able to examine whether player 2 has found the word
# to guess. Give a definition of the function has_won which, given a candidate
# character string, returns the boolean True if all the candidate letters have
# been found, the boolean False otherwise.

def has_won(candidate: str) -> bool:
    '''Preconditions: candidate is a string of letter or "*"
    returns True if all the letters of candidate have been found, False otherwise
    '''
    c: str
    for c in candidate:
        if c == "*":
            return False
    return True

assert has_won("***********") == False
assert has_won("a*ra*a*a*ra") == False
assert has_won("abracadabra") == True

# ---
# Instructions:
# The update function represents the behavior of player 1: depending on a
# candidate word, a letter proposed by player 2 and the word to find, the
# function must return the new candidate word, after revealing the positions
# of the letter proposed. Give a definition of the update function which,
# given three character strings corresponding respectively to the candidate,
# the proposed letter letter and the word to be found word_to_find, returns
# the character string corresponding to the new word.

def update(candidat: str, letter: str, word_to_find: str)->str:
    '''Preconditions: len(letter) == 1 \
    and candidate contains letters or "*" \
    and len(candidate) == len(word_to_find)
    returns a string of the same size as candidate, containing only "*"
    and letters of word_to_find
    '''
    res: str = ""
    pos: int
    for pos in range(len(candidat)):
        if word_to_find[pos] == letter:
            res = res + letter
        else:
            res = res + candidat[pos]
    return res

assert update("***********","a","abracadabra") == 'a**a*a*a**a'
assert update("a**a*a*a**a","b","abracadabra") == 'ab*a*a*ab*a'
assert update("a**a*a*a**a","e","abracadabra") == 'a**a*a*a**a'
assert update("***********","e","abracadabra") == '***********'

# ---
# Instructions:
# We now consider that player 2 has a strategy concerning the order in which
# he proposes letters: this order is defined in the form of a character string
# containing the 26 letters, which he proposes one after the other. We are
# interested in the efficiency of this order, defined as the number of steps
# necessary before finding the hidden word: we can imagine that it is not
# efficient to start with the letters x, y, z or k . Give a definition of the
# function measure_efficiency which, given two character strings representing
# respectively the word to find and an order of proposition of letters, returns
# the number of steps necessary before winning.

def measure_effectiveness(word_to_find: str, order: str) -> int:
    '''Preconditions: word_to_find does not contain "*" \
    and len(order) == 26 letters \
    and order contains all the letters of the alphabet
    returns the number of steps necessary before winning
    '''
    candidate: str = initialise(word_to_find)
    step: int = 0
    letter: str
    while not has_won(candidate):
        letter = order[step]
        candidate = update(candidate, order[step], word_to_find)
        step = step + 1
    return step

assert measure_effectiveness("abracadabra","abcdefghijklmnopqrstuvwxyz") == 18
assert measure_effectiveness("abracadabra","zyxwvutsrqponmlkjihgfedcba") == 26
assert measure_effectiveness("abracadabra","abcdrefghijklmnopqstuvwxyza") == 5
