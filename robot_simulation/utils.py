from typing import Optional
import pygame
from robot_simulation.robot import Robot
from robot_simulation.mode import Mode

def handle_events(robot: Robot, mode: Mode, button_rect: pygame.Rect) -> Mode:
    """Handle quit event, movement keys, and UI button clicks.
    
    Returns the updated mode, or Mode.QUIT if a quit event is detected.
    """
    key_to_direction = {
        pygame.K_UP: "up",
        pygame.K_DOWN: "down",
        pygame.K_LEFT: "left",
        pygame.K_RIGHT: "right",
    }

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return Mode.QUIT
        elif event.type == pygame.KEYDOWN:
            if mode == Mode.MANUAL:
                direction = key_to_direction.get(event.key)
                if direction:
                    robot.move(direction)
            if event.key == pygame.K_t:
                mode = Mode.AUTONOMOUS if mode == Mode.MANUAL else Mode.MANUAL
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                mode = Mode.AUTONOMOUS if mode == Mode.MANUAL else Mode.MANUAL

    return mode
