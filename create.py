import logging
from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()



if __name__ == '__main__':
    sql_create_student_group_table = """
    CREATE TABLE IF NOT EXISTS student_group (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    group_name VARCHAR(30),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );
    """
    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    date_of_birth DATE,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female')),
    group_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (group_id) REFERENCES student_group(group_id)
    	ON DELETE SET NULL 
    	ON UPDATE CASCADE
    );
    """

    sql_create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30)
    );
    """
    sql_create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    subject_name VARCHAR(30),
    teacher_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
    	ON DELETE SET NULL 
    	ON UPDATE CASCADE
    );
    """
    sql_create_grades_table = """
    CREATE TABLE IF NOT EXISTS grades (
    grades_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    grade INTEGER CHECK (grade > 0 AND grade <= 10),
    date_received DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
    	ON DELETE SET NULL 
    	ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
    	ON DELETE SET NULL 
    	ON UPDATE CASCADE
    );
    """
    
    try:
        with create_connection(database) as conn:
            if conn is not None:
                # create  table
                create_table(conn, sql_create_students_table)
                create_table(conn, sql_create_student_group_table)
                create_table(conn, sql_create_teachers_table)
                create_table(conn, sql_create_subjects_table)
                create_table(conn, sql_create_grades_table)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)