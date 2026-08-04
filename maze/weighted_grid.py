from maze.grid import Grid
from maze.weighted_cell import WeightedCell


class WeightedGrid(Grid):
    """A Grid containing WeightedCells."""

    def __init__(self, rows, columns) -> None:
        self.distances = None
        self.maximum = None  # Furthest distance.
        super().__init__(rows, columns)

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

    def background_color_for(self, cell) -> tuple[int, int, int] | None:
        """Returns the background color for a cell."""

        if cell.weight > 1:
            # Red for weighted cells
            return 255, 0, 0

        elif self.distances:
            distance = self.distances[cell]

            if distance is None:
                return None

            if self.maximum is None:
                farthest, self.maximum = self.distances.max()

            if self.maximum == 0:  # Zero division protection in case of a grid with a single cell.
                intensity = 255
            else:
                intensity = int(64 + 191 * (self.maximum - distance) / self.maximum)

            return intensity, intensity, 0

        return None
