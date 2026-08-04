from maze.grid import Grid


class DistanceGrid(Grid):
    """Used for displaying distances in a numeric format."""

    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None  # This needs to be set to cell's distances.

    def contents_of(self, cell):
        """Returns the distance of a cell as one of the following:

        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f, g, h, i, j, k, l,
        m, n, o, p, q, r, s, t, u, v, w, x, y, z.
        """

        if self.distances is not None and self.distances[cell] is not None:
            return str_base(self.distances[cell], 36)
        else:
            return super().contents_of(cell)


# Because we’re limited to one ASCII character for the body of the
# cell, we format the distance as a base-36 integer.
# This lets us represent distances up to 35 using a single character.

# Additional code to format cell distance as base 36
# (from https://stackoverflow.com/questions/2063425):

def str_base(number, base):
    if number < 0:
        return '-' + str_base(-number, base)
    else:
        (d, m) = divmod(number, base)
        if d:
            return str_base(d, base) + digit_to_char(m)
        else:
            return digit_to_char(m)


def digit_to_char(digit):
    if digit < 10:
        return chr(ord('0') + digit)
    else:
        return chr(ord('a') + digit - 10)
