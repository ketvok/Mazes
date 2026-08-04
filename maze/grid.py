import os
import random
from PIL import Image, ImageDraw
from maze.cell import Cell


DRAW_BACKGROUND = 0


class Grid(object):
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows  # number of rows
        self.columns = columns  # number of columns
        self.grid = self.prepare_grid()
        self.configure_cells()

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

    def contents_of(self, cell) -> str:
        """Returns a string representation of the contents of the given cell."""

        return " "

    def background_color_for(self, cell):
        """Returns a background color for the given cell."""

        return None

    def to_s(self) -> None:
        """Prints a string representation of the grid."""

        output = "+" + "---+" * self.columns + "\n"  # Initialize output buffer to be the top boundary of the grid.
        for row in self.each_row():
            top = "|"  # Bodies and eastern walls for row's cells. Initialize to the western boundary of the row.
            bottom = "+"  # Southern boundaries for row's cells. Initialize to the row's southwest corner.
            for cell in row:
                body = " " + self.contents_of(cell) + " "
                east_boundary = " " if cell.linked_to(cell.east) else "|"
                top += body + east_boundary
                south_boundary = "   " if cell.linked_to(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"
        print(output)

    def to_png(self, cell_size: int = 32) -> None:  # Cell size is in pixels.
        """Generates a PNG image of the grid."""

        img_width = cell_size * self.columns
        img_height = cell_size * self.rows
        background = (220, 220, 220)  # Light gray
        wall = (0, 0, 0)  # Black
        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)  # Create a new image.
        draw = ImageDraw.Draw(img)  # Create an object that can be used to draw in the given image.

        # Paint cells and draw borders:
        for mode in range(2):  # First pass draws the cell background, second pass draws the walls.
            for cell in self.each_cell():
                x1 = cell.column * cell_size
                y1 = cell.row * cell_size
                x2 = (cell.column + 1) * cell_size
                y2 = (cell.row + 1) * cell_size

                if mode == DRAW_BACKGROUND:
                    color = self.background_color_for(cell)
                    draw.rectangle((x1, y1, x2, y2), fill = color if color is not None else background)
                else:
                    if not cell.north:
                        draw.line([x1, y1, x2, y1], wall, 1, None)
                    if not cell.west:
                        draw.line([x1, y1, x1, y2], wall, 1, None)
                    if not cell.linked_to(cell.east):
                        draw.line([x2, y1, x2, y2], wall, 1, None)
                    if not cell.linked_to(cell.south):
                        draw.line([x1, y2, x2, y2], wall, 1, None)

        img.show()  # Display this image.

    def deadends(self) -> list[Cell]:
        """Returns a list of dead ends."""

        return [cell for cell in self.each_cell() if len(cell.links) == 1]

    def braid(self, p = 1.0) -> None:
        """
        Removes dead ends from the grid by braiding them.

        The probability of braiding a given cell is given by the parameter p (0.0 - 1.0). A p value of 1.0 will braid
        every cell in the grid.
        """

        deadends = self.deadends()
        random.shuffle(deadends)

        for cell in deadends:
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
