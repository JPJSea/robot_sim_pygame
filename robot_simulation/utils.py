import pygame
from .robot import Robot
from .mode import Mode
from .config import Config
from .grid import Grid

import pygame
import pygame_gui
from .robot import Robot
from .mode import Mode
from .config import Config
from .grid import Grid

def handle_events(
    robot: Robot,
    mode: Mode,
    button_rect: pygame.Rect,
    grid: Grid,
    manager: pygame_gui.UIManager
) -> Mode:
    key_to_direction = {
        pygame.K_UP: "up",
        pygame.K_DOWN: "down",
        pygame.K_LEFT: "left",
        pygame.K_RIGHT: "right",
    }
    # Get all events once
    events = pygame.event.get()
    for event in events:
        # Pass each event to the UI manager so it updates its widgets.
        manager.process_events(event)
        
        if event.type == pygame.QUIT:
            return Mode.QUIT
        elif event.type == pygame.KEYDOWN:
            if mode == Mode.MANUAL:
                direction = key_to_direction.get(event.key)
                if direction:
                    robot.move(direction)
            if event.key == pygame.K_t:
                # Toggle mode with the T key
                mode = Mode.AUTONOMOUS if mode == Mode.MANUAL else Mode.MANUAL
                if mode == Mode.MANUAL:
                    grid.clear_goal()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the click is on the toggle button
            if button_rect is not None and button_rect.collidepoint(event.pos):
                mode = Mode.AUTONOMOUS if mode == Mode.MANUAL else Mode.MANUAL
                if mode == Mode.MANUAL:
                    grid.clear_goal()
            # If in Autonomous mode, allow setting the goal by clicking on the grid
            if mode == Mode.AUTONOMOUS:
                mouse_x, mouse_y = event.pos
                grid_x = mouse_x // Config.CELL_SIZE
                grid_y = mouse_y // Config.CELL_SIZE
                if grid.is_empty(grid_x, grid_y):
                    grid.set_goal(grid_x, grid_y)
    return mode
