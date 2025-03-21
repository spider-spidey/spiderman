fact(sunny).
fact(warm).

rule(play_outside) :- fact(sunny), fact(warm).
rule(stay_inside) :- fact(rainy).

forward_chaining(Goal) :-
    rule(Goal),
    write('Goal achieved: '), write(Goal), nl;
    write('Goal cannot be achieved.').

start :-
    write('Enter your goal (play_outside/stay_inside): '),
    read(Goal),
    forward_chaining(Goal).
