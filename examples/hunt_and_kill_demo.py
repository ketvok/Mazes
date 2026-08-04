from maze.grid import Grid
from algorithms.hunt_and_kill import HuntAndKill


grid = Grid(20, 20)
algorithm = HuntAndKill()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

# grid.to_s()
grid.to_png()
