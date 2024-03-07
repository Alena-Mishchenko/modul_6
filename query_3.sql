SELECT student_group.group_id, student_group.group_name, subj.subject_name, ROUND( AVG(grades.grade),2) AS average_grade_group
FROM student_group
JOIN students ON student_group.group_id = students.group_id
JOIN grades ON students.student_id = grades.student_id
JOIN subjects subj ON grades.subject_id = subj.subject_id
WHERE subj.subject_name = 'Quality manager'
GROUP BY student_group.group_id,  subj.subject_name;
