SELECT s.first_name, s.last_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects subj ON g.subject_id = subj.subject_id
WHERE subj.subject_name = 'Quality manager'
GROUP BY s.student_id
ORDER BY average_grade DESC
LIMIT 1;
