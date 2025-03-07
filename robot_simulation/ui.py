import pygame
import pygame_gui
from pygame import Surface
from robot_simulation.config import Config
from robot_simulation.grid import Grid
from robot_simulation.robot import Robot
from robot_simulation.mode import Mode


class GameUI:
    def __init__(self, screen_size: tuple[int, int], grid_width: int, manager: pygame_gui.UIManager):
        self.screen_width, self.screen_height = screen_size
        self.grid_width = grid_width
        self.button_column_width = self.screen_width - self.grid_width
        self.manager = manager

        # Create a persistent instruction box in the button column.
        # It will be positioned at (grid_width + 20, 20) with a fixed size.
        self.instruction_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect(
                (self.grid_width + 20, 20), (self.button_column_width - 40, 100)),
            manager=self.manager,
            html_text="",
            container=None,
            wrap_to_height=True
        )

        # Create a persistent toggle button rectangle.
        padding = Config.BUTTON_PADDING
        self.button_rect = pygame.Rect(
            0, 0, Config.BUTTON_WIDTH, Config.BUTTON_HEIGHT)
        # Place it at the bottom-right of the button column.
        button_area_right = self.grid_width + self.button_column_width
        self.button_rect.bottomright = (
            button_area_right - padding, self.screen_height - padding)

    def update_instructions(self, mode: Mode) -> None:
        """Update the instruction text in the text box based on the mode."""
        if mode == Mode.MANUAL:
            new_text = "Manual Mode: Use arrow keys to move the robot."
        elif mode == Mode.AUTONOMOUS:
            new_text = "Autonomous Mode: Click on the grid to place the goal."
        else:
            new_text = ""
        self.instruction_box.set_text(new_text)

    def draw(self, screen: Surface) -> None:
        """Update and draw UI elements. The manager will draw the persistent instruction box."""
        self.manager.update(1 / 60)
        self.manager.draw_ui(screen)


def render_screen(screen: Surface, grid: Grid, robot: Robot, mode: Mode, manager: pygame_gui.UIManager) -> pygame.Rect:
    screen_width, screen_height = screen.get_size()

    screen.fill((255, 255, 255))  # White background for the screen

    grid_width = Config.GRID_WIDTH * Config.CELL_SIZE
    # Remaining width for the button column
    button_column_width = screen_width - grid_width

    grid.draw(screen)

    # Draw the goal if it has been set
    grid.draw_goal(screen)

    # Button column area
    button_area = pygame.Rect(
        grid_width, 0, button_column_width, screen_height)
    # Button column background
    pygame.draw.rect(screen, Config.GREEN, button_area)

    # Set up the font and instruction text based on the mode
    instruction_text = ""
    if mode == Mode.MANUAL:
        instruction_text = "Manual Mode: Use arrow keys to move the robot."
    elif mode == Mode.AUTONOMOUS:
        instruction_text = "Autonomous Mode: Click on the grid to place the goal."

    # Create the UITextBox widget for instruction text
    instruction_box = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect(
            (grid_width + 20, 20), (button_column_width - 40, 100)),
        manager=manager,
        html_text=instruction_text,  # Set the mode-dependent instruction text
        container=None,
        wrap_to_height=True  # Allow text to wrap to fit the box's height
    )

    # Button to toggle between Manual and Autonomous modes
    padding = Config.BUTTON_PADDING
    button_width = Config.BUTTON_WIDTH
    button_height = Config.BUTTON_HEIGHT

    button_rect = pygame.Rect(0, 0, button_width, button_height)
    button_rect.bottomright = (
        button_area.right - padding, button_area.bottom - padding)

    # Draw the toggle button
    button_rect = draw_toggle_button(
        screen, mode, button_rect.x, button_rect.y, button_width, button_height)

    # Draw the robot inside the grid area
    robot.draw(screen)

    # Update and draw the UI elements using pygame_gui
    manager.update(1 / 60)  # Update the manager for this frame
    manager.draw_ui(screen)  # Draw the UI on the screen

    pygame.display.flip()
    return button_rect


def draw_toggle_button(screen: Surface, mode: Mode, x: int, y: int, button_width: int, button_height: int) -> pygame.Rect:
    font = pygame.font.Font(None, 36)
    button_text = "Manual" if mode == Mode.AUTONOMOUS else "Auto"

    button_color = Config.RED
    text_color = Config.WHITE

    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)

    text_surface = font.render(button_text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect
