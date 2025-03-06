import pygame
import random

from .config import Config


class Grid:
    """Represents the grid where the robot navigates, with obstacles placed."""
    
    def __init__(self, width, height):
        """Initializes the grid dimensions and sets it as empty."""
        self.width = width
        self.height = height
        self.grid = self._initialize_grid()

    def _initialize_grid(self):
        """Creates an empty grid (all cells are 0 for empty)."""
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def add_obstacles_randomly(self, num_obstacles):
        """Randomly places obstacles on the grid."""
        obstacles_added = 0
        while obstacles_added < num_obstacles:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.grid[y][x] == 0:  # Only add obstacle if the cell is empty
                self.grid[y][x] = 1
                obstacles_added += 1

    def add_obstacle_manually(self, x, y):
        """Manually add an obstacle at specified coordinates."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 1


    def draw(self, screen):
        """Draw the grid with obstacles on the pygame window."""
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(col * Config.CELL_SIZE, row * Config.CELL_SIZE, Config.CELL_SIZE, Config.CELL_SIZE)
                color = Config.BLACK if self.grid[row][col] == 1 else Config.WHITE  # Obstacles are black
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Border for each cell


    def is_empty(self, x, y):
        """Checks if a cell at position (x, y) is empty (no obstacle).
        Returns False for out-of-bounds or obstacle coordinates.
        """
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        return self.grid[y][x] == 0
