from constraint import Problem

def map_coloring():
    problem = Problem()

    states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'VIC', 'TAS']
    colors = ['Red', 'Green', 'Blue']

    for state in states:
        problem.addVariable(state, colors)

    constraints = [
        ('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), 
        ('NT', 'Q'), ('SA', 'Q'), ('SA', 'NSW'), 
        ('SA', 'VIC'), ('Q', 'NSW'), ('NSW', 'VIC')
    ]

    for state1, state2 in constraints:
        problem.addConstraint(lambda x, y: x != y, (state1, state2))

    solutions = problem.getSolutions()
    print("Total Solutions:", len(solutions))
    print(solutions[0])

map_coloring()
