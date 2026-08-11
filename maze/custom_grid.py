from maze.grid import Grid
from maze.weighted_cell import WeightedCell


class CustomGrid(Grid):
    """My Grid."""

    def __init__(self, rows, columns) -> None:
        self.distances = None
        self.maximum = None  # Furthest distance
        super().__init__(rows, columns)

    def contents_of(self, cell):
        """
        For testing purposes.

        Returns the distance of a cell or manhattan distance,
        depending on which part of the code is commented.
        """

        if self.distances is not None and self.distances[cell] is not None:
            # Manhattan heuristic. Formula: abs(x1 - x2) + abs(y1 - y2). Hardcoded x2 and y2 for testing purposes.
            # return str_base(abs(cell.row - 1) + abs(cell.column - 11), 36)  # Hardcoded x2 and y2 for testing purposes.

            # Path distance from root.
            return str_base(self.distances[cell], 36)
        else:
            return super().contents_of(cell)

    def prepare_grid(self) -> list[list[WeightedCell]]:
        """Creates a grid of WeightedCell instances."""

        grid = []

        for row in range(self.rows):
            row_cells = []

            for column in range(self.columns):
                cell = WeightedCell(row, column)
                row_cells.append(cell)

            grid.append(row_cells)

        return grid

    def set_distances(self, distances) -> None:
        """Stores distances and the maximum distance."""

        self.distances = distances
        farthest, self.maximum = distances.max()

    # From weighted_grid.py:
    # def background_color_for(self, cell) -> tuple[int, int, int] | None:
    #     """Returns the background color for a cell."""
    #
    #     if cell.weight > 1:
    #         # Red for weighted cells
    #         return (255, 0, 0)
    #
    #     elif self.distances:
    #         distance = self.distances[cell]
    #
    #         if distance is None:
    #             return None
    #
    #         if self.maximum is None:
    #             farthest, self.maximum = self.distances.max()
    #
    #         if self.maximum == 0:  # Zero division protection in case of a grid with a single cell.
    #             intensity = 255
    #         else:
    #             intensity = int(64 + 191 * (self.maximum - distance) / self.maximum)
    #
    #         return (intensity, intensity, 0)
    #
    #     return None

    def background_color_for(self, cell) -> tuple[int, int, int] | None:
        """Returns the background color for a cell."""

        if self.distances is not None and self.distances[cell] is not None:
            if self.maximum == 0:
                farthest, self.maximum = self.distances.max()  # Get farthest cell and it's distance.
            if self.maximum == 0:  # Zero division protection in case of a grid with a single cell.
                return 255, 255, 255
            distance = self.distances[cell]  # Get distance for a given cell.

            # Calculate RGB intensity based on distance
            intensity = float((self.maximum - distance)) / self.maximum  # 0 to 1; distance of 0 means intensity 1.
            dark = round(255 * intensity)  # This component of RGB is darker.
            bright = 128 + round(127 * intensity)  # This component of RGB is brighter.

            # return dark, bright, dark      # green
            # return dark, dark, bright      # blue
            # return bright, dark, bright    # purple
            # return bright, bright, dark    # greenish
            # return dark, bright, bright    # teal
            return bright, dark, dark       # red
            # return bright, bright, bright  # gray
        else:
            return None


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
