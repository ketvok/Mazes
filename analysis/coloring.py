#################
# Colored mazes #
#################


import tkinter as tk
from maze.grid import Grid
from maze.maze_renderer import MazeRenderer
from gui.maze_window import MazeWindow
from maze_generation.wilsons import Wilsons
from pathfinding.dijkstra import dijkstra


grid = Grid(20, 20)
algorithm = Wilsons()
algorithm.on(grid)

start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = dijkstra(start)

grid.braid(0.2)  # Optional.

root = tk.Tk()
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="Coloring")
root.mainloop()
