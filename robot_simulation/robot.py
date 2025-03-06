import pygame
import pygame.gfxdraw
import random

from .config import Config

class Robot:
    """Represents the robot on the grid."""
    
    def __init__(self, grid):
        """Initializes the robot's position and assigns a random color."""
        self.grid = grid
        self.x, self.y = self.random_position()
        min_rgb = 15
        max_rgb = 205
        self.color = (random.randint(min_rgb, max_rgb), random.randint(min_rgb, max_rgb), random.randint(min_rgb, max_rgb))


    def random_position(self):
        """Randomly generates a position for the robot that isn't on an obstacle."""
        while True:
            x = random.randint(0, self.grid.width - 1)
            y = random.randint(0, self.grid.height - 1)
            if self.grid.is_empty(x, y):
                return x, y  # Return position if it's empty (no obstacle)

    def draw(self, screen):
        """Draw the robot as a circle on the grid."""
        radius = Config.CELL_SIZE // 2  # Radius of the robot, half of cell size
        center_x = self.x * Config.CELL_SIZE + radius  # X center of the circle
        center_y = self.y * Config.CELL_SIZE + radius  # Y center of the circle
        # Draw filled circle with antialiasing
        pygame.gfxdraw.filled_circle(screen, center_x, center_y, radius, self.color)
        # Draw circle outline with antialiasing
        # pygame.gfxdraw.aacircle(screen, center_x, center_y, radius, (0, 0, 0))