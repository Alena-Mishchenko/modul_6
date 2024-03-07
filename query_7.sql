SELECT g.grade, s.first_name, s.last_name, sg.group_name, subj.subject_name
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects subj ON g.subject_id = subj.subject_id
JOIN student_group sg ON s.group_id = sg.group_id
WHERE subj.subject_name = 'Quality manager' AND sg.group_id = 1;