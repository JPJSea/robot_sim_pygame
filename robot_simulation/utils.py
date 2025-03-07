import pygame
import pygame_gui
from .robot import Robot
from .mode import Mode
from .config import Config
from .grid import Grid
from .ui import GameUI
from .path_planner import PathPlanner


def handle_events(
    robot: Robot,
    mode: Mode,
    grid: Grid,
    manager: pygame_gui.UIManager,
    game_ui: GameUI
) -> Mode:
    key_to_direction = {
        pygame.K_UP: "up",
        pygame.K_DOWN: "down",
        pygame.K_LEFT: "left",
        pygame.K_RIGHT: "right",
    }
    events = pygame.event.get()
    for event in events:
        manager.process_events(event)
        if event.type == pygame.QUIT:
            return Mode.QUIT
        elif event.type == pygame.KEYDOWN:
            if mode == Mode.MANUAL:
                direction = key_to_direction.get(event.key)
                if direction:
                    robot.move(direction)
            if event.key == pygame.K_t:
                mode = Mode.AUTONOMOUS if mode == Mode.MANUAL else Mode.MANUAL
                if mode == Mode.MANUAL:
                    grid.clear_goal()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Note: The toggle button is now managed by pygame_gui but
            # this is still needed for the goal setting
            if mode == Mode.AUTONOMOUS:
                mouse_x, mouse_y = event.pos
                grid_x = mouse_x // Config.CELL_SIZE
                grid_y = mouse_y // Config.CELL_SIZE
                if grid.is_empty(grid_x, grid_y):
                    grid.set_goal(grid_x, grid_y)

                    start = (robot.x, robot.y)
                    goal = (grid_x, grid_y)
                    robot.path = PathPlanner.bfs(grid, start, goal)
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == game_ui.toggle_button:
                mode = Mode.AUTONOMOUS if mode == Mode.MANUAL else Mode.MANUAL
                if mode == Mode.MANUAL:
                    grid.clear_goal()
    return mode
