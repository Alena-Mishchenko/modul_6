SELECT subj.subject_name,  t.first_name, t.last_name
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects subj ON g.subject_id = subj.subject_id
JOIN teachers t ON subj.teacher_id = t.teacher_id
WHERE s.student_id = 1 AND t.last_name = 'Spencer'
GROUP BY subj.subject_name;