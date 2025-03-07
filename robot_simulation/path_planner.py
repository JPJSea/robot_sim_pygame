from collections import deque
from robot_simulation.grid import Grid

class PathPlanner:
    @staticmethod
    def bfs(grid: Grid, start: tuple[int, int], goal: tuple[int, int]) -> list[str]:
        """
        Perform Breadth-First Search (BFS) to find the shortest path from start to goal on the grid.

        Parameters:
            grid (Grid): The grid instance containing obstacle information.
            start (tuple[int, int]): Starting coordinates (x, y) of the robot.
            goal (tuple[int, int]): Goal coordinates (x, y) to reach.

        Returns:
            list[str]: A list of directions ('up', 'down', 'left', 'right') representing the shortest path.
                       Returns an empty list if no path exists.
        """
        directions = [(0, -1, "up"), (0, 1, "down"), (-1, 0, "left"), (1, 0, "right")]
        queue = deque([(start, [])])
        visited = set([start])

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == goal:
                return path

            for dx, dy, direction in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < grid.width and 0 <= ny < grid.height and
                        grid.is_empty(nx, ny) and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [direction]))

        return []