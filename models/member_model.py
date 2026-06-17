from pymysql import Error
from pymysql.err import IntegrityError


def authenticate_member(db, login_id, password):
    if db is None or db.connection is None:
        print("Database connection is not available.")
        return None

    try:
        with db.connection.cursor() as cursor:
            query = """
            SELECT login_id, name
            FROM member
            WHERE login_id = %s
              AND password = %s
            """
            cursor.execute(query, (login_id, password))
            return cursor.fetchone()
    except Error as error:
        print(f"Member authentication error: {error}")
        return None


def find_member_by_login_id(db, login_id):
    if db is None or db.connection is None:
        print("Database connection is not available.")
        return None

    try:
        with db.connection.cursor() as cursor:
            query = """
            SELECT login_id, password, name
            FROM member
            WHERE login_id = %s
            """
            cursor.execute(query, (login_id,))
            return cursor.fetchone()
    except Error as error:
        print(f"Member find error: {error}")
        return None


def create_member(db, login_id, password, name):
    if db is None or db.connection is None:
        print("Database connection is not available.")
        return False

    try:
        with db.connection.cursor() as cursor:
            query = """
            INSERT INTO member (login_id, password, name)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (login_id, password, name))

        db.connection.commit()
        return True
    except IntegrityError as error:
        print(f"Member create integrity error: {error}")
        return False
    except Error as error:
        print(f"Member create error: {error}")
        return False
