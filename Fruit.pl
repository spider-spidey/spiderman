% Facts: Fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(kiwi, brown).
fruit_color(lemon, yellow).
fruit_color(watermelon, green).

% Rule to find the color of a fruit
find_color(Fruit) :-
    fruit_color(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl, fail.

% Rule to find fruits of a particular color
find_fruit(Color) :-
    fruit_color(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl, fail.

% Prevent further backtracking
find_color(_) :- !.
find_fruit(_) :- !.
