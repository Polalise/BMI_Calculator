from pymysql import Error


class MemberModel:
    """DB access for members."""

    def __init__(self, database):
        self.database = database

    def find_by_user_id(self, user_id):
        if self.database.connection is None:
            print("데이터베이스 연결이 없습니다.")
            return None

        try:
            with self.database.connection.cursor() as cursor:
                query = """
                SELECT id, user_id, password, name, created_at, activation_type
                FROM members
                WHERE user_id = %s
                """
                cursor.execute(query, (user_id,))
                return cursor.fetchone()
        except Error as error:
            print(f"회원 조회 중 오류 발생: {error}")
            return None

    def create_member(self, user_id, password, name):
        if self.database.connection is None:
            print("데이터베이스 연결이 없습니다.")
            return None

        try:
            with self.database.connection.cursor() as cursor:
                query = """
                INSERT INTO members (user_id, password, name)
                VALUES (%s, %s, %s)
                """
                cursor.execute(query, (user_id, password, name))
                member_id = cursor.lastrowid

            self.database.connection.commit()
            return member_id
        except Error as error:
            print(f"회원 저장 중 오류 발생: {error}")
            return None
