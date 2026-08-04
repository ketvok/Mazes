from maze.grid import Grid
from algorithms.binary_tree import BinaryTree


grid = Grid(20, 20)
algorithm = BinaryTree()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

# grid.to_s()
grid.to_png()
