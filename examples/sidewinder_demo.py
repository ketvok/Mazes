import tkinter as tk
from maze.grid import Grid
from algorithms.sidewinder import Sidewinder


grid = Grid(20, 20)
algorithm = Sidewinder()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

# grid.to_s()
root = tk.Tk()

grid.to_png(parent=root, title="Maze - Sidewinder")
root.mainloop()
