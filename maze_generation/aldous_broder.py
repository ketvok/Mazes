from maze.grid import Grid


class AldousBroder:
    """
    Aldous-Broder algorithm for maze generation.

    Fast start, slow finish.
    """

    def on(self, grid: Grid) -> None:
        cell = grid.random_cell()  # Start at a random cell
        unvisited = grid.size() - 1  # Initiate unvisited count (all cells minus the starting cell)
        while unvisited > 0:
            neighbor = cell.random_neighbour()
            if len(neighbor.links) == 0:
                cell.link(neighbor)
                unvisited -= 1
            cell = neighbor
