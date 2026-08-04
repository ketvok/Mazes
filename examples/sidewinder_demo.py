from maze.grid import Grid
from algorithms.sidewinder import Sidewinder


grid = Grid(20, 20)
algorithm = Sidewinder()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

# grid.to_s()
grid.to_png()
