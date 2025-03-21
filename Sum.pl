sum(0,0).
sum(N,Sum):-
    N>0,
    N1 is N-1,
    sum(N1,S1),
    Sum is S1+N.
start:-
    write('Enter a Number:'),
    read(N),
    sum(N,Sum),
    write('Sum of Integers from 1 to '),write(N),write(' is '),write(Sum),nl.
