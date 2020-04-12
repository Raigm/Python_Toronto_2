def add_greeting(L=[]):
    """ (list) -> NoneType

    Append 'hello' to L and print L.

    >>> L = ['hi', 'bonjour']
    >>> f(L)
    >>> L
    ['hi', 'bonjour', 'hello']
    """

    L.append('hello')
    print(L)

print(add_greeting(["hola"]))
print(add_greeting())
print(add_greeting())