import sqlite3
from contextlib import contextmanager

database = 'homework6.sqlite'


@contextmanager
def create_connection(db_file):
    try:
        """ create a database connection to a SQLite database """
        conn = sqlite3.connect(db_file)
        yield conn
        # conn.rollback()
        conn.close()
    except sqlite3.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection{err}")


if __name__ =="__main__":
    with create_connection("homework6.sqlite") as conn:
        print(conn)