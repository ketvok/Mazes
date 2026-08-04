from maze.grid import Grid
from algorithms.aldous_broder import AldousBroder


grid = Grid(20, 20)
algorithm = AldousBroder()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

# grid.to_s()
grid.to_png()
