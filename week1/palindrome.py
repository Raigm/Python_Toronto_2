

def reverse(s):
    """str -> str

    Return a reverse version of the string

    >>>reverse("hola")
    "aloh"
    """
    return s[::-1]

def is_palindrome(word):
    ''''
    1.reverse the word
    2.compare both
    (str) -> bool
    >>>is_palindrome("non")
    True
    >>>is_palindrome("hola")
    False
    '''
    reverse = word[::-1]
    if word == reverse:
        print("Palindrome!")
    else:
        print("Not palindrome")


def is_palindrome2(word):
    ''''
    (str) -> bool
    1.reverse the word
    2.compare both

    Return True if palindrome
    (str) -> bool
    >>>is_palindrome2("non")
    True
    >>>is_palindrome2("hola")
    False
    '''
    n = len(word)

    print(word[:n//2]==reverse(word[n-n//2:]))


def is_palindrome3(word):
    """
    (str)-> bool
    1. comparin indexes firs to last and so on
    2. Stop when j < i
    >>> is_palindrome3("kayak")
    "True"
    """
    i = 0
    j = len(word) - 1
    while i < j and word[i]==word[j]:
        i = i +1
        j = j - 1
    print( j <= i)


word = "kaya"
# is_palindrome(word)
is_palindrome2(word)
is_palindrome3(word)






