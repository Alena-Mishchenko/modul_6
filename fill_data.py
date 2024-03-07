from datetime import datetime
from faker import Faker
import logging
from random import randint, choice
from sqlite3 import Error
from connect import create_connection


database = 'homework6.sqlite'
fake= Faker()
num_students = 50
num_groups = 3
num_teachers = 5
num_subjects = 8
num_grades_per_student = 20

def generate_student_groups(num_groups):
    student_groups = []
    for i in range(num_groups):
        group_name = fake.word()   # add a unique identifier to the group name
        description = fake.text()
        group = (group_name, description)
        student_groups.append(group)
    return student_groups

def generate_students(num_students,num_groups):
    students = []
    for _ in range(num_students):
        student = (
            fake.first_name(),
            fake.last_name(),
            fake.date_of_birth(),
            choice(['Male', 'Female']),
            randint(1, num_groups)  
        )
        students.append(student)
    return students


def generate_teachers(num_teachers):
    teachers = []
    for _ in range(num_teachers):
        teacher = (
            fake.first_name(),
            fake.last_name()
        )
        teachers.append(teacher)
    return teachers

def generate_subjects(num_subjects, num_teachers):
    subjects = []
    for _ in range(num_subjects):
        subject = (
            fake.job(),  
            randint(1, num_teachers) 
        )
        subjects.append(subject)
    return subjects

def generate_grades(num_students, num_subjects):
    grades = []
    for student_id in range(1, num_students + 1):
        for subject_id in range(1, num_subjects + 1):
            grade = (
                student_id,
                subject_id,
                randint(1, 10), 
                fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')  
            )
            grades.append(grade)
    return grades


def insert_data(conn, sql,data):
    cur = conn.cursor()
    try:
        cur.executemany(sql,data)
        conn.commit()
    except Error as e:
        logging.error(e)
        conn.rollback()
    finally:
        cur.close()
        # conn.close()


if __name__ == '__main__':
    sql_insert_group_table = """
    INSERT INTO  student_group (group_name,description) VALUES(?,?);
    """
    sql_insert_students = """
    INSERT INTO students (first_name,last_name, date_of_birth,gender,group_id) VALUES(?,?,?,?,?);
    """
    # sql_insert_group_table = """
    # INSERT INTO  student_group (group_name,description) VALUES(?,?);
    # """
    sql_insert_teachers_table = """
    INSERT INTO teachers (first_name ,last_name ) VALUES(?,?);
    """
    sql_insert_subjects_table = """
    INSERT INTO subjects (subject_name, teacher_id)VALUES(?,?);
    """
    sql_insert_grades_table = """
    INSERT INTO grades (student_id, subject_id, grade ,date_received) VALUES(?,?,?,?);
    """
 
    try:
        with create_connection(database) as conn:
            if conn is not None:
                students_data = generate_students(num_students,num_groups )
                student_groups_data = generate_student_groups(num_groups)
                teachers_data = generate_teachers(num_teachers)
                subjects_data = generate_subjects(num_subjects, num_teachers)
                grades_data = generate_grades(num_students, num_subjects)

                insert_data(conn, sql_insert_students, students_data)
                insert_data(conn, sql_insert_group_table, student_groups_data)
                insert_data(conn, sql_insert_teachers_table, teachers_data)
                insert_data(conn, sql_insert_subjects_table, subjects_data)
                insert_data(conn, sql_insert_grades_table, grades_data)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)






