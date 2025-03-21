from collections import deque

def is_valid(state, capacity):
    return 0 <= state[0] <= capacity[0] and 0 <= state[1] <= capacity[1]

def bfs(capacity, start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (jug1, jug2), path = queue.popleft()

        if (jug1, jug2) == goal:
            return path + [(jug1, jug2)]

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        moves = [
            (capacity[0], jug2), (jug1, capacity[1]), (0, jug2), (jug1, 0),
            (max(0, jug1 - (capacity[1] - jug2)), min(capacity[1], jug1 + jug2)),
            (min(capacity[0], jug1 + jug2), max(0, jug2 - (capacity[0] - jug1)))
        ]

        for move in moves:
            if is_valid(move, capacity):
                queue.append((move, path + [(jug1, jug2)]))

    return "No solution"

capacity = (4, 3)
start = (0, 0)
goal = (2, 0)
print(bfs(capacity, start, goal))
