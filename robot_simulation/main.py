import random
import pygame
import pygame.gfxdraw

from .config import Config
from .robot import Robot
from .grid import Grid
from robot_simulation.ui import render_screen
from robot_simulation.utils import handle_events
from robot_simulation.mode import Mode


def initialize_game():
    """Initialize the game environment, create grid and robot."""
    # Initialize grid and place obstacles
    grid = Grid(Config.GRID_WIDTH, Config.GRID_HEIGHT)
    grid.add_obstacles_randomly(15)

    robot = Robot(grid)

    return grid, robot

def main():
    pygame.init()

    screen_width = Config.GRID_WIDTH * Config.CELL_SIZE + Config.BUTTON_WIDTH + 40
    screen_height = Config.GRID_HEIGHT * Config.CELL_SIZE
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simulated Robot Navigation")

    grid, robot = initialize_game()
    mode = Mode.MANUAL

    while mode != Mode.QUIT:
        button_rect = render_screen(screen, grid, robot, mode)

        mode = handle_events(robot, mode, button_rect)

        if mode == Mode.AUTONOMOUS:
            random_direction = random.choice(["up", "down", "left", "right"])
            robot.move(random_direction)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()