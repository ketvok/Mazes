import tkinter as tk
from maze.grid import Grid
from algorithms.link_all import LinkAll


grid = Grid(20, 20)
algorithm = LinkAll()
algorithm.on(grid)

# grid.to_s()
root = tk.Tk()

grid.to_png(parent=root, title="Maze - Link All")
root.mainloop()
