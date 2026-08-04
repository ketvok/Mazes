from random import choice
from maze.grid import Grid


class Wilsons:
    """
    Wilson's algorithm for maze generation.
    Slow start, fast finish.
    """

    def on(self, grid:Grid) -> None:
        unvisited = []
        for cell in grid.each_cell():
            unvisited.append(cell)  # Add all cells to the unvisited list.

        first = choice(unvisited)  # Choose a random cell as the starting cell.
        unvisited.remove(first)  # Remove the starting cell from the unvisited list.

        while len(unvisited) > 0:
            cell = choice(unvisited)  # Choose a random cell as the current cell.
            path = [cell]  # Initialize the path with the current cell.

            while cell in unvisited:
                cell = cell.random_neighbour()  # Choose a random neighboring cell.
                try:
                    position = path.index(cell)  # Check if the cell is already in the path...
                    path = path[:position + 1]  # ...if it is, truncate the path at that position.
                except ValueError:
                    path.append(cell)  # If the cell is not in the path, add it to the path.

            for index in range(len(path) - 1):
                path[index].link(path[index + 1])  # Link the cells in the path.
                unvisited.remove(path[index])  # Remove the linked cells from the unvisited list.
