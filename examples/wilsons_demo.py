import tkinter as tk
from maze.grid import Grid
from algorithms.wilsons import Wilsons


grid = Grid(20, 20)
algorithm = Wilsons()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

# grid.to_s()
root = tk.Tk()

grid.to_png(parent=root, title="Maze - Wilson's")
root.mainloop()
