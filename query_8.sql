SELECT t.first_name, t.last_name, 
ROUND(AVG(grades.grade), 2) AS average_grade_teachers_subject, subj.subject_name
FROM teachers t
JOIN subjects subj ON subj.teacher_id = t.teacher_id
JOIN grades ON grades.subject_id = subj.subject_id
WHERE t.last_name = 'Martinez' 
GROUP BY subject_name;