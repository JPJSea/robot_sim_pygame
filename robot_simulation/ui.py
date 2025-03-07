import pygame
import pygame_gui
from pygame import Surface
from .config import Config
from .mode import Mode
from .grid import Grid
from .robot import Robot


class GameUI:
    def __init__(self, screen_size: tuple[int, int], grid_width: int, manager: pygame_gui.UIManager):
        self.screen_width, self.screen_height = screen_size
        self.grid_width = grid_width
        self.button_column_width = self.screen_width - self.grid_width
        self.manager = manager

        padding = Config.BUTTON_PADDING

        self.instruction_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((self.grid_width + 20, 20), (self.button_column_width - 40, 100)),
            manager=self.manager,
            html_text="",
            container=None,
            wrap_to_height=True
        )

        self.toggle_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.grid_width + padding, self.screen_height - Config.BUTTON_HEIGHT - padding),
                (Config.BUTTON_WIDTH, Config.BUTTON_HEIGHT)
            ),
            text="Auto",
            manager=self.manager,
            container=None
        )

    def update_instructions(self, mode: Mode) -> None:
        if mode == Mode.MANUAL:
            text = "Manual Mode: Use arrow keys to move the robot."
        elif mode == Mode.AUTONOMOUS:
            text = "Autonomous Mode: Click on the grid to place the goal."
        else:
            text = ""
        self.instruction_box.set_text(text)

    def update_toggle_button(self, mode: Mode) -> None:
        if mode == Mode.MANUAL:
            self.toggle_button.set_text("Auto")
        elif mode == Mode.AUTONOMOUS:
            self.toggle_button.set_text("Manual")

    def draw(self, screen: Surface) -> None:
        self.manager.update(1/60)
        self.manager.draw_ui(screen)



def render_screen(screen: Surface, grid: Grid, robot: Robot, mode: Mode, manager: pygame_gui.UIManager) -> None:
    screen_width, screen_height = screen.get_size()
    screen.fill((255, 255, 255))

    grid.draw(screen)
    grid.draw_goal(screen)

    # Draw the button column background.
    grid_width = Config.GRID_WIDTH * Config.CELL_SIZE
    button_area = pygame.Rect(grid_width, 0, screen_width - grid_width, screen_height)
    pygame.draw.rect(screen, Config.GREEN, button_area)

    robot.draw(screen)