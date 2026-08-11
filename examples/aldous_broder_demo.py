import tkinter as tk
from maze.grid import Grid
from algorithms.aldous_broder import AldousBroder


grid = Grid(20, 20)
algorithm = AldousBroder()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

# grid.to_s()
root = tk.Tk()

grid.to_png(parent=root, title="Maze - Aldous Broder")
root.mainloop()
