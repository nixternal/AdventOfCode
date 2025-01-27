#!/usr/bin/env python

from collections import deque


def wall_or_open(coords: tuple, fav_num: int) -> bool:
    x, y = coords
    a = ((x * x) + (3 * x) + (2 * x * y) + y + (y * y)) + fav_num
    return not bin(a).strip('0b').count('1') % 2


def part_one() -> int:
    start = (1, 1)
    finish = (31, 39)
    grid = [['.'] * 50 for _ in range(50)]
    for x in range(50):
        for y in range(50):
            if wall_or_open((x, y), 1350):
                grid[x][y] = '.'
            else:
                grid[x][y] = '#'

    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while deque:
        x, y, dist = queue.popleft()

        # Check if we've reached the finish
        if (x, y) == finish:
            return dist

        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the new position is in bounds & not a wall or visited
            if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.' and
                    (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1


def part_two() -> int:
    start = (1, 1)
    finish = (31, 39)
    grid = [['.'] * 50 for _ in range(50)]
    for x in range(50):
        for y in range(50):
            if wall_or_open((x, y), 1350):
                grid[x][y] = '.'
            else:
                grid[x][y] = '#'

    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while deque:
        x, y, dist = queue.popleft()

        # Check if we've reached the finish
        if (x, y) == finish:
            break

        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the new position is in bounds & not a wall or visited
            if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.' and
                    (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

            if dist == 50:
                return len(visited)

    return -1


if __name__ == "__main__":
    print("Part 1:", part_one())  # 92
    print("Part 2:", part_two())  # 124
