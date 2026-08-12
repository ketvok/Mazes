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

    def distances(self) -> "Distances":
        """Compute unweighted shortest paths using simplified Dijkstra's algorithm."""

        weights = Distances(self)  # Shortest distances to the start node. Starts with self as start (distance 0).
        frontier = [self]  # Start with self as the only cell in the frontier.

        while frontier:
            new_frontier = []

            for cell in frontier:
                for linked_cell in cell.links:
                    if weights[linked_cell] is None and weights[cell] is not None:
                        weights[linked_cell] = weights[cell] + 1
                        new_frontier.append(linked_cell)

            frontier = new_frontier  # Update the frontier. If new_frontier is empty, the loop will terminate.

        return weights
