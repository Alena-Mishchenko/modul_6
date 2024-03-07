SELECT subjects.subject_name, teachers.first_name, teachers.last_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE teachers.last_name = 'Spencer';