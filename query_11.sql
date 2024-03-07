SELECT  ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects subj ON g.subject_id = subj.subject_id
JOIN teachers t ON subj.teacher_id = t.teacher_id
WHERE s.student_id = 1 AND t.last_name = 'Martinez';