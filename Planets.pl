planet('Mercury', rocky, 57.9, 0).
planet('Venus', rocky, 108.2, 0).
planet('Earth', rocky, 149.6, 1).
planet('Mars', rocky, 227.9, 2).
planet('Jupiter', gas_giant, 778.3, 95).
planet('Saturn', gas_giant, 1427.0, 146).
planet('Uranus', ice_giant, 2871.0, 27).
planet('Neptune', ice_giant, 4495.1, 14).

find_type(Planet) :-
    planet(Planet, Type, _, _),
    write(Planet), write(' is a '), write(Type), write(' planet.'), nl.

find_distance(Planet) :-
    planet(Planet, _, Distance, _),
    write(Planet), write(' is '), write(Distance), write(' million km from the Sun.'), nl.

find_moons(Planet) :-
    planet(Planet, _, _, Moons),
    write(Planet), write(' has '), write(Moons), write(' moons.'), nl.
