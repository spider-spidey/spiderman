def a_star(graph, start, goal, heuristics):
    open_list = set([start])
    closed_list = set()
    g = {start: 0}
    parent = {start: start}
    
    while open_list:
        current = min(open_list, key=lambda x: g[x] + heuristics[x])
        if current == goal:
            path = []
            while parent[current] != current:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]
        
        open_list.remove(current)
        closed_list.add(current)
        
        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue
            tentative_g = g[current] + cost
            if neighbor not in open_list:
                open_list.add(neighbor)
            elif tentative_g >= g.get(neighbor, float('inf')):
                continue
            parent[neighbor] = current
            g[neighbor] = tentative_g
    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': [('F', 2)],
    'F': []
}

heuristics = {
    'A': 7, 'B': 6, 'C': 4, 'D': 3, 'E': 1, 'F': 0
}

print("Path:", a_star(graph, 'A', 'F', heuristics))
