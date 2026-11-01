import random
from maze.cell import Cell


class Grid(object):
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows  # number of rows
        self.columns = columns  # number of columns
        self.grid = self.prepare_grid()
        self.configure_cells()
        self.distances = None
        self.maximum = 0  # Furthest distance

    def prepare_grid(self) -> list[list[Cell]]:
        """Sets up a simple two-dimensional array of Cell instances."""

        grid = []
        
        for row in range(self.rows):
            row_cells = []
            
            for column in range(self.columns):
                cell = Cell(row, column)
                row_cells.append(cell)

            grid.append(row_cells)

        return grid

    def configure_cells(self) -> None:
        """Tells each cell who its immediate neighbors are to the
        north, south, east, and west."""

        for cell in self.each_cell():
            row = cell.row
            column = cell.column
            cell.north = self[row - 1, column]
            cell.south = self[row + 1, column]
            cell.east = self[row, column + 1]
            cell.west = self[row, column - 1]

    def __getitem__(self, key) -> Cell | None:
        """Grants access to arbitrary cell in the grid using []."""

        row, column = key
        if row < 0 or row > self.rows - 1:
            return None
        if column < 0 or column > self.columns - 1:
            return None

        return self.grid[row][column]

    def random_cell(self) -> Cell | None:
        """Returns random cell."""

        row = random.randrange(0, self.rows)
        column = random.randrange(0, self.columns)

        return self[row, column]

    def size(self) -> int:
        """Returns the number of cells in the grid."""
        
        return self.rows * self.columns

    def each_row(self):
        """Yields each row in the grid in turn."""

        for row in range(self.rows):
            yield self.grid[row]

    def each_cell(self):
        """Yields each cell in the grid in turn."""

        for row in self.each_row():
            for cell in row:
                if cell is not None:
                    yield cell

    def cell_at(self, row, column) -> Cell | None:
        """Returns cell in a specified location."""

        if not (0 <= row < self.rows):
            return None
        if not (0 <= column < self.columns):
            return None

        return self.grid[row][column]

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

    def dead_ends(self) -> list[Cell]:
        """Returns a list of dead ends."""

        return [cell for cell in self.each_cell() if len(cell.links) == 1]

    def braid(self, p = 1.0) -> None:
        """
        Removes dead ends from the grid by braiding them.

        The probability of braiding a given cell is given by the parameter p (0.0 - 1.0). A p value of 1.0 will braid
        every cell in the grid.
        """

        dead_ends = self.dead_ends()
        random.shuffle(dead_ends)

        for cell in dead_ends:
            # Check to see that it's still a dead end (as an earlier iteration of the loop may have already linked it to
            # a neighboring dead end)
            if (len(cell.links) != 1 or  # If it's not a dead end (i.e., it's linked to more than one cell),
                random.random() > p):    # or if we've chosen not to braid it,
                    continue             # skip it.

            neighbors = [n for n in cell.neighbors() if not cell.linked_to(n)]  # Get all unlinked neighbors.

            # We can kill two birds with one stone and improve the aesthetics of the maze a bit by preferring to link
            # two dead-end cells together:
            best = [n for n in neighbors if len(n.links) == 1]  # Get all neighbors that are linked to only one other cell.
            if not best:
                best = neighbors

            if best:
                neighbor = random.choice(best)  # Pick a random neighbor.
                cell.link(neighbor)  # Braid it!

    def set_distances(self, distances) -> None:
        """Stores distances and the maximum distance."""

        self.distances = distances
        farthest, self.maximum = distances.max()
