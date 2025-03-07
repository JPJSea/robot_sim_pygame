from os import confstr
import pygame
from pygame import Surface
from robot_simulation import config
from robot_simulation.config import Config
from robot_simulation.grid import Grid
from robot_simulation.robot import Robot
from robot_simulation.mode import Mode

def render_screen(screen: Surface, grid: Grid, robot: Robot, mode: Mode) -> pygame.Rect:
    screen_width, screen_height = screen.get_size()

    screen.fill((255, 255, 255))

    grid_width = Config.GRID_WIDTH * Config.CELL_SIZE

    button_column_width = screen_width - grid_width

    grid.draw(screen)

    button_area = pygame.Rect(grid_width, 0, button_column_width, screen_height)
    pygame.draw.rect(screen, Config.GREEN, button_area)

    padding = Config.BUTTON_PADDING
    button_width = Config.BUTTON_WIDTH
    button_height = Config.BUTTON_HEIGHT

    button_rect = pygame.Rect(0, 0, button_width, button_height)
    button_rect.bottomright = (button_area.right - padding, button_area.bottom - padding)

    button_rect = draw_toggle_button(screen, mode, button_rect.x, button_rect.y, button_width, button_height)

    robot.draw(screen)

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
