from random import choice
from maze.distances import Distances


class Cell(object):
    """Defines a cell in a grid."""

    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
        self._links: dict["Cell", bool] = {}
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.weight = 1  # Default movement cost to this cell.

    def link(self, cell, bidi = True) -> "Cell":
        """Link the given cell to this cell."""

        self._links[cell] = True
        if bidi:
            cell.link(self, False)  # Pass False to avoid infinite recursion.

        return self

    def unlink(self, cell, bidi = True) -> "Cell":
        """Unlink the given cell from this cell."""

        del self._links[cell]
        if bidi:
            cell.unlink(self, False)  # Pass False to avoid infinite recursion.

        return self

    @property
    def links(self) -> list["Cell"]:
        """Return a list of linked cells."""

        return list(self._links.keys())

    def linked_to(self, cell) -> bool:
        """Return True if the given cell is linked to this cell."""

        return cell in self._links

    def neighbors(self) -> list["Cell"]:
        """Return a list of this cell's immediate neighbors."""

        neighbor_cells = []

        if self.north:
            neighbor_cells.append(self.north)
        if self.south:
            neighbor_cells.append(self.south)
        if self.east:
            neighbor_cells.append(self.east)
        if self.west:
            neighbor_cells.append(self.west)

        return neighbor_cells
        
    def random_neighbour(self) -> "Cell | None":
        """Return a random neighbor of this cell."""

        if len(self.neighbors()) == 0:
            return None
        else:
            return choice(self.neighbors())
