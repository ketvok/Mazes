#################
# Colored mazes #
#################


import tkinter as tk
from maze.colored_grid import ColoredGrid
from maze.maze_renderer import MazeRenderer
from gui.maze_window import MazeWindow
from algorithms.wilsons import Wilsons


grid = ColoredGrid(20, 20)
algorithm = Wilsons()
algorithm.on(grid)

start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()

grid.braid(0.2)  # Optional.

root = tk.Tk()
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="Coloring")
root.mainloop()
