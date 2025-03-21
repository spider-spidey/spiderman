edge(a, b, 4).
edge(a, c, 3).
edge(b, d, 5).
edge(b, e, 12).
edge(c, f, 7).
edge(d, g, 9).
edge(e, g, 4).
edge(f, g, 2).

heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 5).
heuristic(d, 3).
heuristic(e, 7).
heuristic(f, 4).
heuristic(g, 0).

best_first_search(Start, Goal, Path) :-
    bestfs([[Start]], Goal, Path).

bestfs([[Goal|Path]|_], Goal, [Goal|Path]).
bestfs([CurrentPath|OtherPaths], Goal, FinalPath) :-
    CurrentPath = [CurrentNode|_],
    findall([Next,CurrentNode|CurrentPath],
            (edge(CurrentNode, Next, _), \+ member(Next, CurrentPath)),
            Paths),
    append(OtherPaths, Paths, NewPaths),
    sort_paths(NewPaths, SortedPaths),
    bestfs(SortedPaths, Goal, FinalPath).

sort_paths(Paths, SortedPaths) :-
    maplist(path_heuristic, Paths, Heuristics),
    pairs_keys_values(Pairs, Heuristics, Paths),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, SortedPaths).

path_heuristic([Node|_], H) :-
    heuristic(Node, H).

start :-
    write('Enter Start Node: '),
    read(Start),
    write('Enter Goal Node: '),
    read(Goal),
    best_first_search(Start, Goal, Path),
    write('Best First Search Path: '), write(Path), nl.
