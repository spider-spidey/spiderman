from collections import deque

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def swap(state, x1, y1, x2, y2):
    new_state = [row[:] for row in state]
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    moves = [(0, 1, 'Right'), (0, -1, 'Left'), (1, 0, 'Down'), (-1, 0, 'Up')]

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        
        visited.add(tuple(map(tuple, state)))
        x, y = find_zero(state)

        for dx, dy, move in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                new_state = swap(state, x, y, nx, ny)
                if tuple(map(tuple, new_state)) not in visited:
                    queue.append((new_state, path + [move]))
    return None

start_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
result = bfs(start_state, goal_state)

print("Solution:", result if result else "No Solution")
