

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
    >>>palindrome("non")
    True
    >>>palindrome("hola")
    False
    '''
    reverse = word[::-1]
    if word == reverse:
        print("Palindrome!")
    else:
        print("Not palindrome")


def is_palindrome2(word):
    ''''
    1.reverse the word
    2.compare both

    Return True if palindrome
    (str) -> bool
    >>>palindrome("non")
    True
    >>>palindrome("hola")
    False
    '''
    n = len(word)

    print(word[:n//2]==reverse(word[n-n//2:]))


word= "kayak"
# is_palindrome(word)
is_palindrome2(word)






