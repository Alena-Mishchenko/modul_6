SELECT s.first_name, s.last_name, subj.subject_name
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects subj ON g.subject_id = subj.subject_id
WHERE s.student_id = 1 
GROUP BY s.student_id,subj.subject_name;
