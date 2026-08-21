class Distances:
    """Stores distances from a root cell to reachable cells."""

    def __init__(self, root):
        self.root = root
        self._cells = {root: 0}  # Dictionary for storing the distances from the root to other cells.

    def __getitem__(self, cell) -> int | None:
        """Return the stored distance for 'cell', or 'None' if it is unknown, using []."""

        if cell in self._cells.keys():
            return self._cells[cell]

        return None
        
    def __setitem__(self, cell, distance):
        """Store the distance from the root to 'cell' using []."""

        self._cells[cell] = distance
        
    def cells(self) -> list:
        """Return a list of cells that have stored distance values."""

        return list(self._cells.keys())
        
    def path_to(self, goal) -> "Distances":
        """
        Finds the shortest path to a goal cell.

        This method calculates the shortest path from the root cell to a specified
        goal cell by backtracking the distances stored for each cell. It creates
        a new Distances object to store the path, starting from the root cell,
        and fills it with cells leading back to the root.

        For an unweighted maze, multiple neighbors may satisfy the condition of
        having a shorter distance to root than the current cell, but they all
        have the same distance: exactly one less than the current cell. If both
        A and B have distance goal_distance - 1, either one produces a shortest
        path. The method simply chooses whichever appears first in current.links.

        Parameters:
            goal: The target cell to which the path should be traced.

        Returns:
            A Distances object containing the path from the root cell to the
            specified goal cell, with the distances for each cell along the path.
        """

        current = goal  # Start from the goal cell as current cell.
        breadcrumbs = Distances(self.root)  # Create a new Distances object, add root to it, and...
        breadcrumbs[current] = self._cells[current]  # ...add goal cell to it.

        while current != self.root:
            for neighbor in current.links:
                if neighbor in self._cells:  # Avoid KeyError if neighbor is not in _cells (e.g., in A*).
                    if self._cells[neighbor] < self._cells[current]:  # If neighboring cell is closer to root than current cell...
                        breadcrumbs[neighbor] = self._cells[neighbor]  # ...add it to breadcrumbs.
                        current = neighbor  # Move position to added cell.
                        break

        return breadcrumbs
        
    def max(self) -> tuple:
        """
        Identifies the cell with the maximum distance from the root cell.

        This method iterates through a collection of cells and determines which
        cell has the maximum associated distance value. It returns the cell and
        its corresponding distance.

        Returns:
            A tuple containing the cell with the maximum distance and the
            associated distance value.
        """

        max_distance = 0
        max_cell = self.root

        for cell in self._cells:
            if self._cells[cell] > max_distance:
                max_cell = cell
                max_distance = self._cells[cell]

        return max_cell, max_distance
