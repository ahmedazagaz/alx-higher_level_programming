class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Constructor 
        Args:
            size (int): Size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  # Size of the square

