from itertools import permutations

def tsp(graph):
    n = len(graph)
    cities = range(n)
    min_cost = float('inf')
    best_path = []
    for path in permutations(cities):
        cost = sum(graph[path[i]][path[i+1]] for i in range(n-1)) + graph[path[-1]][path[0]]
        if cost < min_cost:
            min_cost = cost
            best_path = path
    return best_path, min_cost

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp(graph)
print("Best Path:", path)
print("Minimum Cost:", cost)
