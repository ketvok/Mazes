from PIL import Image, ImageDraw


class MazeRenderer:
    """Renders a grid-based maze as an image."""

    def __init__(self, cell_size: int = 16):
        self.cell_size = cell_size

    def render(self, grid) -> Image.Image:
        """
        Converts the grid into an image representation with cells and walls.

        Args:
            grid: The grid object to render.

        Returns:
            A PIL Image object containing the rendered maze.
        """

        width = self.cell_size * grid.columns
        height = self.cell_size * grid.rows

        background = (220, 220, 220)
        wall = (0, 0, 0)

        image = Image.new(
            "RGB",
            (width + 1, height + 1),
            background
        )

        draw = ImageDraw.Draw(image)

        for cell in grid.each_cell():
            x1 = cell.column * self.cell_size
            y1 = cell.row * self.cell_size
            x2 = (cell.column + 1) * self.cell_size
            y2 = (cell.row + 1) * self.cell_size

            color = grid.background_color_for(cell)
            draw.rectangle(
                (x1, y1, x2, y2),
                fill=color if color is not None else background
            )

        for cell in grid.each_cell():
            x1 = cell.column * self.cell_size
            y1 = cell.row * self.cell_size
            x2 = (cell.column + 1) * self.cell_size
            y2 = (cell.row + 1) * self.cell_size

            if not cell.north:
                draw.line((x1, y1, x2, y1), fill=wall, width=1)

            if not cell.west:
                draw.line((x1, y1, x1, y2), fill=wall, width=1)

            if not cell.linked_to(cell.east):
                draw.line((x2, y1, x2, y2), fill=wall, width=1)

            if not cell.linked_to(cell.south):
                draw.line((x1, y2, x2, y2), fill=wall, width=1)

        return image
