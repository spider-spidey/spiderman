symptom(john, fever).
symptom(john, cough).
symptom(john, fatigue).
symptom(susan, headache).
symptom(susan, fever).
symptom(susan, nausea).

disease(flu) :- symptom(_, fever), symptom(_, cough), symptom(_, fatigue).
disease(migraine) :- symptom(_, headache), symptom(_, nausea).
disease(covid) :- symptom(_, fever), symptom(_, cough), symptom(_, fatigue), symptom(_, headache).

diagnose(Patient, Disease) :-
    symptom(Patient, fever),
    symptom(Patient, cough),
    disease(Disease),
    write(Patient), write(' might have '), write(Disease), nl.

start :-
    write('Enter patient name: '),
    read(Patient),
    (diagnose(Patient, Disease) -> true ; write('No diagnosis found')).
