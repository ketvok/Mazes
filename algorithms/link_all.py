from maze.grid import Grid


class LinkAll:
    """
    Algorithm that links every cell with every neighbor.

    Results in a grid with no walls.
    """

    def on(self, grid: Grid) -> None:
        for cell in grid.each_cell():
            for neighbor in cell.neighbors():
                cell.link(neighbor)
