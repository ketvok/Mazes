import tkinter as tk
from maze.grid import Grid
from maze.maze_renderer import MazeRenderer
from gui.maze_window import MazeWindow
from maze_generation.binary_tree import BinaryTree
from maze.text_renderer import TextRenderer

grid = Grid(20, 20)
algorithm = BinaryTree()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

renderer = TextRenderer()
print(renderer.render(grid))

root = tk.Tk()
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="Binary Tree Demo")
root.mainloop()
