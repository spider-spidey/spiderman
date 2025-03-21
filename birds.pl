bird(sparrow, yes).
bird(eagle, yes).
bird(penguin, no).
bird(ostrich, no).
bird(parrot, yes).
bird(peacock, yes).
bird(kiwi, no).
bird(duck, yes).

can_fly(Bird) :-
    bird(Bird, yes),
    write(Bird), write(' can fly.'), nl.

can_fly(Bird) :-
    bird(Bird, no),
    write(Bird), write(' cannot fly.'), nl.

print_flying_birds :-
    bird(Bird, yes),
    write(Bird), write(' can fly.'), nl,
    fail.
print_flying_birds.

print_non_flying_birds :-
    bird(Bird, no),
    write(Bird), write(' cannot fly.'), nl,
    fail.
print_non_flying_birds.
