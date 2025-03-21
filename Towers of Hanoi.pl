hanoi(1, Source, Destination, _) :-
    write('Move disk 1 from '), write(Source), write(' to '), write(Destination), nl.

hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Destination),
    write('Move disk '), write(N), write(' from '), write(Source), write(' to '), write(Destination), nl,
    hanoi(N1, Auxiliary, Destination, Source).

start :-
    write('Enter number of disks: '),
    read(N),
    hanoi(N, 'A', 'C', 'B').
