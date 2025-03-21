goal_state(state(_, _, _, yes)).

move(state(Pos, BoxPos, on_floor, HasBanana),
     walk(Pos, NewPos),
     state(NewPos, BoxPos, on_floor, HasBanana)).

move(state(Pos, Pos, on_floor, HasBanana),
     push(Pos, NewPos),
     state(NewPos, NewPos, on_floor, HasBanana)).

move(state(Pos, Pos, on_floor, HasBanana),
     climb,
     state(Pos, Pos, on_box, HasBanana)).

move(state(Pos, Pos, on_box, no),
     grab,
     state(Pos, Pos, on_box, yes)).

solve(State, Moves) :- solve(State, [], Moves).

solve(State, _, []) :- goal_state(State).
solve(State, Visited, [Move|Moves]) :-
    move(State, Move, NextState),
    \+ member(NextState, Visited),
    solve(NextState, [NextState|Visited], Moves).

