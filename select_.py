import sqlite3
from sqlite3 import Error
import logging
from connect import create_connection

database = 'homework6.sqlite'
def execute_query(sql: str):
    try:
        with create_connection(database) as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute(sql)
                return cursor.fetchall()
            else:
                print("Error! Cannot create the database connection.")
    except Error as e:
        logging.error(e)


    
if __name__ == '__main__':
    sql_average_grade_1 = '''
    SELECT s.first_name, s.last_name, ROUND(AVG(g.grade),2) AS average_grade
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    GROUP BY s.student_id
    ORDER BY average_grade DESC
    LIMIT 5;
    '''
    result = execute_query(sql_average_grade_1)
    if result:
        print("Середній бал студентів:")
        for row in result:
            print(row)
    else:
        print("Немає даних.")

    sql_max_average_grade_2 = '''
    SELECT s.first_name, s.last_name, ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    WHERE subj.subject_name = 'Quality manager'
    GROUP BY s.student_id
    ORDER BY average_grade DESC
    LIMIT 1;
    '''
    print (execute_query(sql_max_average_grade_2))
 

    sql_average_grade_group_3 = '''
    SELECT student_group.group_id, student_group.group_name, subj.subject_name, ROUND( AVG(grades.grade),2) AS average_grade_group
    FROM student_group
    JOIN students ON student_group.group_id = students.group_id
    JOIN grades ON students.student_id = grades.student_id
    JOIN subjects subj ON grades.subject_id = subj.subject_id
    WHERE subj.subject_name = 'Quality manager'
    GROUP BY student_group.group_id,  subj.subject_name;
    '''
    result = execute_query(sql_average_grade_group_3)
    if result:
        print("Середній бал групах з певного предмета:")
        for row in result:
            print(row)
    else:
        print("Немає даних.")


    sql_all_average_grade_4 = '''
    SELECT  ROUND( AVG(grades.grade),2) AS all_average_grade
    FROM grades;
    '''
    print (execute_query(sql_all_average_grade_4))

    sql_subject_teacher_5 = '''
    SELECT subjects.subject_name
    FROM subjects
    JOIN teachers ON subjects.teacher_id = teachers.teacher_id
    WHERE teachers.last_name = 'Spencer';
    '''
    print (execute_query(sql_subject_teacher_5))

    sql_list_students_group_6 = '''
    SELECT s.first_name, s.last_name
    FROM students s
    JOIN student_group g ON s.group_id = g.group_id
    WHERE s.group_id = 1;
    '''
    result = execute_query(sql_list_students_group_6)
    if result:
        print("Cписок студентів по групі:")
        for row in result:
            print(row)
    else:
        print("Немає даних.")


    sql_grade_students_group_7 = '''
    SELECT g.grade, s.first_name, s.last_name, sg.group_name, subj.subject_name
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    JOIN student_group sg ON s.group_id = sg.group_id
    WHERE subj.subject_name = 'Quality manager' AND sg.group_id = 1;
    '''
    result = execute_query(sql_grade_students_group_7)
    if result:
        print("Оцінки студентів у окремій групі з певного предмета:")
        for row in result:
            print(row)
    else:
        print("Немає даних.")       

    sql_verage_grade_teachers_subject_8 = '''
    SELECT t.first_name, t.last_name, 
    ROUND(AVG(grades.grade), 2) AS average_grade_teachers_subject, subj.subject_name
    FROM teachers t
    JOIN subjects subj ON subj.teacher_id = t.teacher_id
    JOIN grades ON grades.subject_id = subj.subject_id
    WHERE t.last_name = 'Martinez' 
    GROUP BY subject_name;
    '''
    print (execute_query(sql_verage_grade_teachers_subject_8))  

    sql_courses_student_9 = '''
    SELECT s.first_name, s.last_name, subj.subject_name
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    WHERE s.student_id = 1 
    GROUP BY s.student_id,subj.subject_name;
    '''
    print (execute_query(sql_courses_student_9))  

    sql_subjects_student_by_teacher_10 = '''
    SELECT subj.subject_name,  t.first_name, t.last_name
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    JOIN teachers t ON subj.teacher_id = t.teacher_id
    WHERE s.student_id = 1 AND t.last_name = 'Spencer'
    GROUP BY subj.subject_name;
    '''
    print (execute_query(sql_subjects_student_by_teacher_10))  

    sql_average_grade_11 = '''
    SELECT  ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    JOIN teachers t ON subj.teacher_id = t.teacher_id
    WHERE s.student_id = 1 AND t.last_name = 'Martinez';
    '''
    print (execute_query(sql_average_grade_11))  

    sql_grade_students_subject_last_lesson_12 = '''
    SELECT g.grade, s.first_name, s.last_name, sg.group_name, subj.subject_name
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    JOIN student_group sg ON s.group_id = sg.group_id
    WHERE subj.subject_name = 'Quality manager' AND sg.group_id = 1 
    ORDER BY g.date_received DESC
    LIMIT 1;
    '''
    print (execute_query(sql_grade_students_subject_last_lesson_12))  