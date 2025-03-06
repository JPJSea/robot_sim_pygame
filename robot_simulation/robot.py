import pygame
import pygame.gfxdraw
import random

from .config import Config

class Robot:
    """Represents the robot on the grid."""
    _DIRECTIONS = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }
    
    def __init__(self, grid):
        """Initializes the robot's position and assigns a random color."""
        self.grid = grid
        self.x, self.y = self.random_position()
        min_rgb = 15
        max_rgb = 205
        self.color = (random.randint(min_rgb, max_rgb), random.randint(min_rgb, max_rgb), random.randint(min_rgb, max_rgb))

    @classmethod
    def get_directions(cls):
        """Safely return a copy of the directions map."""
        return cls._DIRECTIONS.copy()

    def move(self, direction: str):
        """Move the robot if the target cell is empty."""
        directions = self.get_directions()

        if direction not in directions:
            raise ValueError(f"Invalid direction: {direction}")

        dx, dy = directions[direction]
        new_x = self.x + dx
        new_y = self.y + dy

        if self._can_move_to(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def _can_move_to(self, x: int, y: int) -> bool:
        """Check if the robot can move to the specified cell."""
        return (
            0 <= x < self.grid.width and
            0 <= y < self.grid.height and
            self.grid.is_empty(x, y)
        )

    def random_position(self):
        """Randomly generates a position for the robot that isn't on an obstacle."""
        while True:
            x = random.randint(0, self.grid.width - 1)
            y = random.randint(0, self.grid.height - 1)
            if self.grid.is_empty(x, y):
                return x, y

    def draw(self, screen):
        """Draw the robot as a circle on the grid."""
        radius = Config.CELL_SIZE // 2
        center_x = self.x * Config.CELL_SIZE + radius
        center_y = self.y * Config.CELL_SIZE + radius
        # Draw filled circle with antialiasing
        pygame.gfxdraw.filled_circle(screen, center_x, center_y, radius, self.color)
        # Draw circle outline with antialiasing
        # pygame.gfxdraw.aacircle(screen, center_x, center_y, radius, (0, 0, 0))