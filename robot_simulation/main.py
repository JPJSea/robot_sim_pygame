import random
import pygame
import pygame.gfxdraw
import pygame_gui

from .config import Config
from .robot import Robot
from .grid import Grid
from robot_simulation.ui import render_screen, GameUI
from robot_simulation.utils import handle_events
from robot_simulation.mode import Mode


def initialise_game():
    """Initialise the game environment, create grid and robot."""
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

    manager = pygame_gui.UIManager((screen_width, screen_height))

    grid, robot = initialise_game()
    mode = Mode.MANUAL

    grid_width = Config.GRID_WIDTH * Config.CELL_SIZE
    game_ui = GameUI((screen_width, screen_height), grid_width, manager)

    clock = pygame.time.Clock()
    while mode != Mode.QUIT:
        time_delta = clock.tick(60) / 1000.0

        mode = handle_events(robot, mode, grid, manager, game_ui)

        # Update persistent UI elements.
        game_ui.update_instructions(mode)
        game_ui.update_toggle_button(mode)

        render_screen(screen, grid, robot, mode, manager)
        
        manager.update(time_delta)
        manager.draw_ui(screen)
        
        if mode == Mode.AUTONOMOUS:
            random_direction = random.choice(["up", "down", "left", "right"])
            robot.move(random_direction)
            
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
