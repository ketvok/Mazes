class Distances:
    """Stores distances from a root cell to reachable cells."""

    def __init__(self, root):
        self.root = root
        self._cells = {}  # Dictionary for storing the distances from the root to other cells.
        self._cells[root] = 0  # Distance from root to root is 0.
        
    def __getitem__(self, cell) -> int | None:
        """Return the stored distance for `cell`, or `None` if it is unknown, using []."""

        if cell in self._cells.keys():
            return self._cells[cell]

        return None
        
    def __setitem__(self, cell, distance):
        """Store the distance from the root to `cell` using []."""

        self._cells[cell] = distance
        
    def cells(self) -> list:
        """Return a list of cells that have stored distance values."""

        return list(self._cells.keys())
        
    def path_to(self, goal) -> "Distances":
        """
        Return the shortest path from the root to `goal` as a Distances object.

        The returned object contains the cells on the path, with their stored distances from the root.
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
        
    def max(self):
        """Return the cell farthest from the root and its distance."""

        max_distance = 0
        max_cell = self.root

        for cell in self._cells:
            if self._cells[cell] > max_distance:
                max_cell = cell
                max_distance = self._cells[cell]

        return max_cell, max_distance
