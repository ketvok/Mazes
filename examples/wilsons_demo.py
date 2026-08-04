from maze.grid import Grid
from algorithms.wilsons import Wilsons


grid = Grid(20, 20)
algorithm = Wilsons()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

# grid.to_s()
grid.to_png()
