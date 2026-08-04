from random import choice
from maze.grid import Grid


class RecursiveBacktracker:
    """
    Recursive backtracker algorithm for maze generation.

    Can require up to twice as much memory as Hunt and Kill algorithm, but is generally going to be faster.
    """

    def on(self, grid: Grid, start_at = None) -> None:
        stack = []
        if start_at is None:
            stack.append(grid.random_cell())
        else:
            stack.append(start_at)

        while stack:
            current_cell = stack[-1]  # The last cell added to the stack is the current cell.
            unvisited_neighbors = [neighbor for neighbor in current_cell.neighbors() if not neighbor.links]
            if not unvisited_neighbors:
                stack.pop()
            else:
                neighbor = choice(unvisited_neighbors)
                current_cell.link(neighbor)
                stack.append(neighbor)
