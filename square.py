#!/usr/bin/python3


class square():
    """
    class representing a square

    Args:
        width(int) - the width of the square
        height(int) - the height of the square
    """

    def __init__(self, width=0, height=0):
        """
        initializes width and height
        """

        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
