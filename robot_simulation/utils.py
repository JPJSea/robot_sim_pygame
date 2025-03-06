import pygame
from pygame import Surface

from robot_simulation.config import Config
from robot_simulation.robot import Robot
from robot_simulation.grid import Grid

def handle_events(robot: Robot) -> bool:
    """Handle quit event and movement keys."""

    key_to_direction = {
        pygame.K_UP: "up",
        pygame.K_DOWN: "down",
        pygame.K_LEFT: "left",
        pygame.K_RIGHT: "right",
    }

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            direction = key_to_direction.get(event.key)
            if direction:
                robot.move(direction)

    return True

def render_screen(screen: Surface, grid: Grid, robot: Robot) -> None:
    """Render the grid and the robot on the screen."""
    screen.fill(Config.WHITE)
    grid.draw(screen)
    robot.draw(screen)
    pygame.display.flip()
