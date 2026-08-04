from maze.grid import Grid


class ColoredGrid(Grid):
    """Used to visualize distances in a colorful format."""

    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None  # This needs to be set to cell's distances
        self.maximum = 0  # Largest distance

    def background_color_for(self, cell) -> tuple[int, int, int] | None:
        """Returns the background color for a cell.

        The color is determined by the distance from the root cell.
        """

        if self.distances is not None and self.distances[cell] is not None:
            if self.maximum == 0:
                farthest, self.maximum = self.distances.max()  # Get farthest cell and it's distance.
            if self.maximum == 0:  # Zero division protection in case of a grid with a single cell.
                return 255, 255, 255
            distance = self.distances[cell]  # Get distance for a given cell.

            # Calculate RGB intensity based on distance
            intensity = float((self.maximum - distance)) / self.maximum  # 0 to 1; distance of 0 means intensity 1.
            dark = round(255 * intensity)  # This component of RGB is darker.
            bright = 128 + round(127 * intensity)  # This component of RGB is brighter.

            #return dark, bright, dark      # green
            #return dark, dark, bright      # blue
            #return bright, dark, bright    # purple
            #return bright, bright, dark    # greenish
            #return dark, bright, bright    # teal
            return bright, dark, dark      # red
            #return bright, bright, bright  # gray
        else:
            return None
