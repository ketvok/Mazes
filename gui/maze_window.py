import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class MazeWindow:
    """
    Represents a window for displaying and interacting with a maze image.

    It resizes the image to fit the window as it is resized and provides a menu to save the
    displayed image.
    """

    def __init__(self, parent, image, title: str = "Maze View"):
        # Keep the original Pillow image. It is used again whenever the window changes size
        # and when the user saves the image.
        self.image = image

        # Toplevel creates a new window that belongs to the existing parent window.
        self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.window.geometry("500x500")
        self.window.minsize(500, 500)

        # Create a canvas object that will display the image.
        self.canvas = tk.Canvas(master=self.window)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Permit the canvas's row and column to grow when the window grows.
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Create an empty image object on the canvas and remember its ID.
        # The actual image is assigned later, after the canvas has a usable size.
        self.image_id = self.canvas.create_image(0, 0, anchor=tk.CENTER)

        # <Configure> is generated when the canvas is resized. Calling our method here
        # keeps the maze centered and scaled to fit the available space.
        self.canvas.bind("<Configure>", self._resize_image)

        # Add the File menu and perform the first image resize.
        self._create_menu()
        self._resize_image()

    def _resize_image(self, event=None) -> None:
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # During the initial layout Tkinter can report a zero-sized canvas. Wait for the
        # next <Configure> event instead of trying to resize to an invalid image size.
        if canvas_width <= 0 or canvas_height <= 0:
            return

        image_width, image_height = self.image.size

        # Calculate one scale factor that fits the image in both dimensions.
        # The 1.0 limit prevents a small image from being enlarged.
        scale = min(
            canvas_width / image_width,
            canvas_height / image_height,
            1.0
        )

        # Convert the scaled dimensions to whole pixels. max(1, ...) guarantees that
        # neither dimension becomes zero after rounding.
        new_size = (
            max(1, int(image_width * scale)),
            max(1, int(image_height * scale))
        )

        # Make a resized copy of the original image.
        # BOX resampling proved to be fast and produce sharp-looking images at the same
        # time.
        resized_image = self.image.resize(new_size, Image.Resampling.BOX)

        # Convert the Pillow image to a Tkinter-compatible image.
        # Store it on self: Tkinter may stop displaying images whose Python reference
        # is removed by the garbage collector.
        self.photo_image = ImageTk.PhotoImage(resized_image)

        # Move the image object's center to the center of the canvas.
        self.canvas.coords(self.image_id, canvas_width / 2, canvas_height / 2)

        # Tell the existing canvas object to display the newly resized image.
        self.canvas.itemconfig(self.image_id, image=self.photo_image)

    def _create_menu(self) -> None:
        # Create a menu bar.
        menubar = tk.Menu(self.window)

        # Create a drop-down menu. tearoff=0 disables the detachable-menu feature.
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(  # Add a menu item to the drop-down menu.
            label="Save As...",
            command=self._save_image
        )

        # Add the drop-down menu to the menu bar under the label "File".
        menubar.add_cascade(
            label="File",
            menu=file_menu
        )

        # Attach the completed menu bar to this particular window.
        self.window.config(menu=menubar)

    def _save_image(self) -> None:
        # Ask the user where to save the original, full-size image.
        save_path = filedialog.asksaveasfilename(
            initialfile=self.window.title(),
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")]
        )

        # If the user cancels the dialog, save_path is empty and nothing is saved.
        if save_path:
            self.image.save(save_path)
