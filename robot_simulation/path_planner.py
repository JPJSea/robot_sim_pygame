from collections import deque
from robot_simulation.grid import Grid

class PathPlanner:
    @staticmethod
    def bfs(grid: Grid, start: tuple[int, int], goal: tuple[int, int]) -> list[str]:
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

        return []  # No path found