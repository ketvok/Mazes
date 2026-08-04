from random import choice
from maze.grid import Grid


class BinaryTree(object):
    """
    Binary tree algorithm for maze generation.

    Mazes it creates have two unbroken corridors, along the northern and eastern borders.
    """

    def on(self, grid: Grid) -> None:
        for cell in grid.each_cell():
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)

            if len(neighbors) > 0:
                neighbor = choice(neighbors)
                cell.link(neighbor)
