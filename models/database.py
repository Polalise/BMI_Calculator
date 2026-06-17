import pymysql
from pymysql import Error

from config import dbSetting


class Database:
    """MariaDB 연결과 공통 DB 작업을 담당합니다."""

    def __init__(self):
        self.connection = None

        try:
            self.connection = pymysql.connect(
                host=dbSetting.DB_HOST,
                database=dbSetting.DB_DATABASE,
                user=dbSetting.DB_USER,
                password=dbSetting.DB_PASSWORD,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor,
            )
            print("MariaDB에 성공적으로 연결되었습니다.")
        except Error as error:
            print(f"MariaDB 연결 중 오류 발생: {error}")

    def save_bmi_record(self, weight, height, bmi, category):
        """BMI 기록을 데이터베이스에 저장합니다."""
        if self.connection is None:
            print("데이터베이스 연결이 없습니다.")
            return False

        try:
            with self.connection.cursor() as cursor:
                query = """
                INSERT INTO bmi_records (weight, height, bmi, category)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (weight, height, bmi, category))

            self.connection.commit()
            return True
        except Error as error:
            print(f"데이터 저장 중 오류 발생: {error}")
            return False

    def get_bmi_records(self, limit=10):
        """최근 BMI 기록을 조회합니다."""
        if self.connection is None:
            print("데이터베이스 연결이 없습니다.")
            return []

        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT *
                FROM bmi_records
                ORDER BY created_at DESC
                LIMIT %s
                """
                cursor.execute(query, (limit,))
                return cursor.fetchall()
        except Error as error:
            print(f"데이터 조회 중 오류 발생: {error}")
            return []

    def close(self):
        """데이터베이스 연결을 종료합니다."""
        if self.connection:
            self.connection.close()
            print("MariaDB 연결이 종료되었습니다.")
