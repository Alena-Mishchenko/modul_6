SELECT s.first_name, s.last_name, g.group_name
FROM students s
JOIN student_group g ON s.group_id = g.group_id
WHERE s.group_id = 1;