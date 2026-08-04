from maze.grid import Grid
from algorithms.recursive_backtracker import RecursiveBacktracker


grid = Grid(20, 20)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

# grid.to_s()
grid.to_png()
