import pygame
import pygame.gfxdraw
import pygame_gui  # Import pygame_gui for UI handling

from .config import Config
from .robot import Robot
from .grid import Grid
from robot_simulation.ui import render_screen, GameUI, draw_toggle_button
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
    screen_height = Config.GRID_HEIGHT * Config.CELL_SIZE  # Height based on grid
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simulated Robot Navigation")

    # Create the UI manager
    manager = pygame_gui.UIManager((screen_width, screen_height))

    grid, robot = initialize_game()
    mode = Mode.MANUAL

    clock = pygame.time.Clock()

    while mode != Mode.QUIT:
        time_delta = clock.tick(60) / 1000.0  # 60 FPS

        button_rect = render_screen(screen, grid, robot, mode, manager)
        mode = handle_events(robot, mode, button_rect, grid, manager)

        # Update the UI manager (it will update all UI widgets)
        manager.update(time_delta)
        manager.draw_ui(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
