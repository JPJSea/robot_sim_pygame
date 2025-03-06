import pygame
from robot_simulation.config import Config
from robot_simulation.robot import Robot

def handle_events(robot: Robot) -> bool:
    """Handle quit event and movement keys."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                robot.move("up")
            elif event.key == pygame.K_DOWN:
                robot.move("down")
            elif event.key == pygame.K_LEFT:
                robot.move("left")
            elif event.key == pygame.K_RIGHT:
                robot.move("right")
    return True

def render_screen(screen, grid, robot):
    """Render the grid and the robot on the screen."""
    screen.fill(Config.WHITE)
    grid.draw(screen)
    robot.draw(screen)
    pygame.display.flip()
