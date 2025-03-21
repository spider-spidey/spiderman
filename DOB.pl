name('Ben','1997-10-10').
name('Gwen','1997-12-30').
name('Peter','2001-08-21').
find_dob(Name):-
    name(Name,DOB),
    write('Date of Birth of '),write(Name),write(' is '),write(DOB),nl.
find_name(DOB):-
    name(Name,DOB),
    write('Name of the Person with DOB '),write(DOB),write(' is '),write(Name),nl.
