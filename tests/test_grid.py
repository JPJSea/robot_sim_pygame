import pytest
from robot_simulation.grid import Grid


@pytest.fixture
def grid():
    """Creates a 5x5 grid for testing."""
    return Grid(5, 5)


def test_grid_initialization(grid):
    """Grid should be initialized with all empty cells."""
    for row in grid.grid:
        assert all(cell == 0 for cell in row)


def test_grid_dimensions(grid):
    """Grid should have correct width and height."""
    assert grid.width == 5
    assert grid.height == 5
    assert len(grid.grid) == 5
    assert len(grid.grid[0]) == 5


def test_manual_obstacle_placement(grid):
    """Manually placed obstacles should appear in the grid."""
    grid.add_obstacle_manually(2, 3)
    assert grid.grid[3][2] == 1

    grid.add_obstacle_manually(0, 0)
    assert grid.grid[0][0] == 1


def test_manual_obstacle_out_of_bounds(grid):
    """Placing obstacles out of bounds should do nothing (no crash)."""
    grid.add_obstacle_manually(-1, 0)
    grid.add_obstacle_manually(5, 5)

    assert len(grid.grid) == 5
    assert len(grid.grid[0]) == 5


def test_random_obstacle_placement(grid):
    """Randomly place obstacles and count them."""
    num_obstacles = 10
    grid.add_obstacles_randomly(num_obstacles)

    # Count actual obstacles
    actual_obstacles = sum(cell == 1 for row in grid.grid for cell in row)

    assert actual_obstacles == num_obstacles


def test_is_empty(grid):
    """is_empty should correctly detect empty and occupied cells."""
    assert grid.is_empty(2, 2) is True

    grid.add_obstacle_manually(2, 2)
    assert grid.is_empty(2, 2) is False


def test_is_empty_out_of_bounds(grid):
    """is_empty should return False for out-of-bounds coordinates."""
    assert grid.is_empty(-1, 0) is False
    assert grid.is_empty(5, 5) is False
