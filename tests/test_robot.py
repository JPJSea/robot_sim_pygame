import unittest
from unittest.mock import MagicMock

from robot_simulation.grid import Grid
from robot_simulation.robot import Robot
from robot_simulation.config import Config

class TestRobot(unittest.TestCase):
    def test_robot_random_color(self):
        robot = Robot(MagicMock())
        color = robot.color
        self.assertTrue(50 <= color[0] <= 205)
        self.assertTrue(50 <= color[1] <= 205)
        self.assertTrue(50 <= color[2] <= 205)

    def test_robot_random_position(self):
        grid = MagicMock()
        grid.is_empty.return_value = True
        robot = Robot(grid)
        grid.is_empty.assert_called_once()
        self.assertIsInstance(robot.x, int)
        self.assertIsInstance(robot.y, int)

    def test_robot_position_not_on_obstacle(self):
        grid = MagicMock()
        grid.is_empty.return_value = True
        robot = Robot(grid)
        grid.is_empty.assert_called_once()
        self.assertTrue(robot.x >= 0 and robot.x < Config.GRID_WIDTH)
        self.assertTrue(robot.y >= 0 and robot.y < Config.GRID_HEIGHT)