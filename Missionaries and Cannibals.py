from collections import deque

def is_valid(state):
    m1, c1, boat, m2, c2 = state
    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
        return False
    if (m1 > 0 and m1 < c1) or (m2 > 0 and m2 < c2):
        return False
    return True

def next_states(state):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    m1, c1, boat, m2, c2 = state
    for m, c in moves:
        if boat == 1:
            new_state = (m1 - m, c1 - c, 0, m2 + m, c2 + c)
        else:
            new_state = (m1 + m, c1 + c, 1, m2 - m, c2 - c)
        if is_valid(new_state):
            yield new_state

def solve():
    start = (3, 3, 1, 0, 0)
    goal = (0, 0, 0, 3, 3)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for next_state in next_states(state):
            queue.append((next_state, path + [state]))

solution = solve()
for step in solution:
    print(step)
