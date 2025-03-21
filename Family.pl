male(john).
male(michael).
male(robert).
male(david).
male(james).

female(lisa).
female(susan).
female(mary).
female(emma).
female(anna).

parent(john, michael).
parent(john, lisa).
parent(mary, michael).
parent(mary, lisa).
parent(michael, david).
parent(michael, susan).
parent(lisa, james).
parent(lisa, emma).
parent(robert, anna).

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

brother(X, Y) :-
    sibling(X, Y),
    male(X).

sister(X, Y) :-
    sibling(X, Y),
    female(X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).


