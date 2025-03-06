import pygame
import pygame.gfxdraw

from .config import Config
from .robot import Robot
from .grid import Grid
from robot_simulation.utils import handle_events, render_screen


def initialize_game():
    """Initialize the game environment, create grid and robot."""
    # Initialize grid and place obstacles
    grid = Grid(Config.GRID_WIDTH, Config.GRID_HEIGHT)
    grid.add_obstacles_randomly(15)

    robot = Robot(grid)

    return grid, robot

def main():
    """Main game loop to initialize the grid and robot, and handle pygame events."""
    
    pygame.init()
    screen = pygame.display.set_mode((Config.GRID_WIDTH * Config.CELL_SIZE, Config.GRID_HEIGHT * Config.CELL_SIZE))
    pygame.display.set_caption("Simulated Robot Navigation")

    grid, robot = initialize_game()

    running = True
    while running:
        running = handle_events(robot)

        render_screen(screen, grid, robot)

    pygame.quit()


if __name__ == "__main__":
    main()