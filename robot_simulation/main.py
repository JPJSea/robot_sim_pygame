import pygame
import random
import pygame.gfxdraw

from .config import Config
from .robot import Robot
from .grid import Grid

def initialize_game():
    """Initialize the game environment, create grid and robot."""
    # Initialize grid and place obstacles
    grid = Grid(Config.GRID_WIDTH, Config.GRID_HEIGHT)
    grid.add_obstacles_randomly(15)  # Add 15 random obstacles

    # Initialize robot with random position
    robot = Robot(grid)

    return grid, robot

def handle_events():
    """Handle all the pygame events like quitting or keypresses."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def render_screen(screen, grid, robot):
    """Render the screen by drawing the grid and the robot."""
    screen.fill(Config.WHITE)  # Fill the screen with white (background color)
    
    # Draw grid and robot
    grid.draw(screen)
    robot.draw(screen)

    # Update the display
    pygame.display.flip()

def main():
    """Main game loop to initialize the grid and robot, and handle pygame events."""
    
    # Initialize pygame and set up the window
    pygame.init()
    screen = pygame.display.set_mode((Config.GRID_WIDTH * Config.CELL_SIZE, Config.GRID_HEIGHT * Config.CELL_SIZE))
    pygame.display.set_caption("Simulated Robot Navigation")

    # Initialize the game (grid, robot)
    grid, robot = initialize_game()

    # Game loop
    running = True
    while running:
        # Handle events (e.g., closing the window)
        running = handle_events()

        # Render the game screen
        render_screen(screen, grid, robot)

    # Quit pygame
    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()