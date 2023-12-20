class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.
        Args:
           size: Length of side of the square. 
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size  # size of the square

