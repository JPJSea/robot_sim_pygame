import pytest

from robot_simulation.grid import Grid
from robot_simulation.robot import Robot


@pytest.fixture
def grid():
    """Creates a 5x5 empty grid for testing."""
    return Grid(5, 5)


@pytest.fixture
def robot(grid):
    """Creates a robot in the grid."""
    return Robot(grid)


def clear_grid(grid):
    """Clear grid obstacles"""
    grid.grid = [[0] * grid.width for _ in range(grid.height)]


def test_initial_position(robot, grid):
    """Robot should start inbounds on an empty cell."""
    assert grid.is_empty(robot.x, robot.y)
    assert 0 <= robot.x < grid.width
    assert 0 <= robot.y < grid.height


def test_robot_does_not_move_into_obstacles(robot, grid):
    """Robot should not move into a cell with an obstacle in any direction."""

    clear_grid(grid)

    # Place robot at known position (center)
    center_x = grid.width // 2
    center_y = grid.height // 2
    robot.x = center_x
    robot.y = center_y

    # Place obstacles in all 4 directions around the robot
    obstacles = {
        "up": (center_x, center_y - 1),
        "down": (center_x, center_y + 1),
        "left": (center_x - 1, center_y),
        "right": (center_x + 1, center_y)
    }

    for direction, (obs_x, obs_y) in obstacles.items():
        grid.grid[obs_y][obs_x] = 1  # Place obstacle

        robot.x, robot.y = center_x, center_y

        # Move robot and assert it didn't move into obstacle
        robot.move(direction)
        assert (robot.x, robot.y) == (center_x, center_y)

        # Clear obstacle
        grid.grid[obs_y][obs_x] = 0


def test_invalid_direction(robot):
    """Robot should raise ValueError for invalid direction."""
    with pytest.raises(ValueError, match="Invalid direction"):
        robot.move("diagonal")


def test_robot_moves_in_all_directions(robot, grid):
    """Place robot in center and check movement in all 4 directions on a clear grid."""

    clear_grid(grid)

    # Place robot in center
    center_x = grid.width // 2
    center_y = grid.height // 2
    robot.x = center_x
    robot.y = center_y

    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    for direction, (dx, dy) in directions.items():
        robot.x, robot.y = center_x, center_y

        robot.move(direction)

        # Assert the robot moved exactly by (dx, dy)
        assert robot.x == center_x + dx
        assert robot.y == center_y + dy


def test_robot_does_not_move_out_of_bounds(robot, grid):
    """Robot should not move out of the grid from corners or edges."""

    robot.x, robot.y = 0, 0
    robot.move("up")
    assert (robot.x, robot.y) == (0, 0)

    robot.move("left")
    assert (robot.x, robot.y) == (0, 0)

    robot.y = grid.height - 1
    robot.move("down")
    assert (robot.x, robot.y) == (0, grid.height - 1)

    robot.x = grid.width - 1
    robot.move("right")
    assert (robot.x, robot.y) == (grid.width - 1, grid.height - 1)

    robot.x, robot.y = 2, 0
    robot.move("up")
    assert (robot.x, robot.y) == (2, 0)