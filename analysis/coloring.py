#################
# Colored mazes #
#################


import tkinter as tk
from maze.colored_grid import ColoredGrid
from algorithms.wilsons import Wilsons


grid = ColoredGrid(20, 20)
algorithm = Wilsons()
algorithm.on(grid)

start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()

grid.braid(0.2)

root = tk.Tk()

grid.to_png(parent=root, title="Coloring")
root.mainloop()
