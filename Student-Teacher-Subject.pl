student_teacher_subject('Alice', 'Mr. Smith', 'Math', 'M101').
student_teacher_subject('Bob', 'Ms. Johnson', 'Physics', 'P102').
student_teacher_subject('Charlie', 'Mr. Smith', 'Math', 'M101').
student_teacher_subject('David', 'Dr. Lee', 'Chemistry', 'C103').
student_teacher_subject('Eva', 'Ms. Johnson', 'Physics', 'P102').

find_teacher(Student) :-
    student_teacher_subject(Student, Teacher, _, _),
    write(Student), write(' is taught by '), write(Teacher), nl.

find_subject(Student) :-
    student_teacher_subject(Student, _, Subject, _),
    write(Student), write(' studies '), write(Subject), nl.

find_subject_code(Student) :-
    student_teacher_subject(Student, _, _, SubjectCode),
    write('Subject code for '), write(Student), write(' is '), write(SubjectCode), nl.
