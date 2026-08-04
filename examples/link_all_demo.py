from maze.grid import Grid
from algorithms.link_all import LinkAll


grid = Grid(20, 20)
algorithm = LinkAll()
algorithm.on(grid)

# grid.to_s()
grid.to_png()
