fact(sunny).
fact(warm).

rule(play_outside) :- fact(sunny), fact(warm).
rule(stay_inside) :- fact(rainy).

backward_chaining(Goal) :-
    (fact(Goal) -> write('Fact known: '), write(Goal), nl;
    rule(Goal) -> write('Goal achieved using rules: '), write(Goal), nl;
    write('Goal cannot be achieved')).

start :-
    write('Enter your goal (play_outside/stay_inside/sunny/warm/rainy): '),
    read(Goal),
    backward_chaining(Goal).
