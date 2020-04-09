class mystr(str):

    def same_start_end(self):
        """(mystr)--> bool
        returns true is same
        >>> s = mystr("abracadabra")
        >>> s.same_start_end(self))
        True
        """
        return self[0] == self[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()