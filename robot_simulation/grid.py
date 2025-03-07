import pygame
import random
from .config import Config
from typing import Optional
from .robot import Robot

class Goal:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def set_position(self, x: int, y: int) -> None:
        """Set the goal position."""
        self.x = x
        self.y = y


class Grid:
    """Represents the grid where the robot navigates, with obstacles placed."""
    
    def __init__(self, width: int, height: int) -> None:
        """Initializes the grid dimensions and sets it as empty."""
        self.width: int = width
        self.height: int = height
        self.grid: list[list[int]] = self._initialize_grid()
        self.robot: Optional["Robot"] = None
        self.goal: Goal = Goal(-1, -1)  # default invalid position

    def draw_goal(self, screen: pygame.Surface) -> None:
        """Draw the goal on the grid."""
        goal_rect: pygame.Rect = pygame.Rect(self.goal.x * Config.CELL_SIZE, self.goal.y * Config.CELL_SIZE, Config.CELL_SIZE, Config.CELL_SIZE)
        pygame.draw.rect(screen, Config.PINK, goal_rect)

    def clear_goal(self):
        self.goal.set_position(-1, -1)

    def _initialize_grid(self) -> list[list[int]]:
        """Creates an empty grid (all cells are 0 for empty)."""
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def add_obstacles_randomly(self, num_obstacles: int) -> None:
        """Randomly places obstacles on the grid."""
        obstacles_added: int = 0
        while obstacles_added < num_obstacles:
            x: int = random.randint(0, self.width - 1)
            y: int = random.randint(0, self.height - 1)
            if self.grid[y][x] == 0:  # Only add obstacle if the cell is empty
                self.grid[y][x] = 1
                obstacles_added += 1

    def add_obstacle_manually(self, x: int, y: int) -> None:
        """Manually add an obstacle at specified coordinates."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 1

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the grid with obstacles on the pygame window."""
        for row in range(self.height):
            for col in range(self.width):
                rect: pygame.Rect = pygame.Rect(col * Config.CELL_SIZE, row * Config.CELL_SIZE, Config.CELL_SIZE, Config.CELL_SIZE)
                color: tuple[int, int, int] = Config.BLUE if self.grid[row][col] == 1 else Config.CREAM
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)

    def is_empty(self, x: int, y: int) -> bool:
        """Checks if a cell at position (x, y) is empty (no obstacle).
        Returns False for out-of-bounds or obstacle coordinates.
        """
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        return self.grid[y][x] == 0

    def set_goal(self, x: int, y: int) -> None:
        """Set the goal position if the clicked cell is empty."""
        if self.is_empty(x, y):
            self.goal.set_position(x, y)