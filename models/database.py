import pymysql
from pymysql import Error

from config import dbSetting


class Database:
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
            self.create_bmi_records_table()
            print("MariaDB에 성공적으로 연결되었습니다.")
        except Error as error:
            print(f"MariaDB connection error: {error}")

    def create_bmi_records_table(self):
        if self.connection is None:
            print("Database connection is not available.")
            return False

        try:
            with self.connection.cursor() as cursor:
                query = """
                CREATE TABLE IF NOT EXISTS bmi_records (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    login_id VARCHAR(50),
                    weight FLOAT NOT NULL,
                    height FLOAT NOT NULL,
                    bmi FLOAT NOT NULL,
                    category VARCHAR(20) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
                cursor.execute(query)

            self.connection.commit()
            return True
        except Error as error:
            print(f"BMI records table create error: {error}")
            return False

    def save_bmi_record(self, login_id, weight, height, bmi, category):
        """BMI 기록을 데이터베이스에 저장합니다."""
        if self.connection is None:
            print("Database connection is not available.")
            return False

        try:
            with self.connection.cursor() as cursor:
                query = """
                INSERT INTO bmi_records (login_id, weight, height, bmi, category)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (login_id, weight, height, bmi, category))

            self.connection.commit()
            return True
        except Error as error:
            print(f"BMI records table create error: {error}")
            return False

    def create_activity_logs_table(self):
        if self.connection is None:
            print("Database connection is not available.")
            return False

        try:
            with self.connection.cursor() as cursor:
                query = """
                CREATE TABLE IF NOT EXISTS activity_logs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    login_id VARCHAR(50),
                    action_type VARCHAR(20) NOT NULL,
                    description VARCHAR(255),
                    request_uri VARCHAR(255),
                    http_method VARCHAR(10),
                    status_code INT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
                cursor.execute(query)

            self.connection.commit()
            return True
        except Error as error:
            print(f"Activity logs table create error: {error}")
            return False

    def save_bmi_record(self, login_id, weight, height, bmi, category):
        if self.connection is None:
            print("Database connection is not available.")
            return False

        try:
            with self.connection.cursor() as cursor:
                query = """
                INSERT INTO bmi_records (login_id, weight, height, bmi, category)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (login_id, weight, height, bmi, category))

            self.connection.commit()
            return True
        except Error as error:
            print(f"BMI record save error: {error}")
            return False

    def get_bmi_records(self, login_id, limit=10):
        """최근 BMI 기록을 조회합니다."""
        if self.connection is None:
            print("Database connection is not available.")
            return []

        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT *
                FROM bmi_records
                WHERE login_id = %s
                ORDER BY created_at DESC
                LIMIT %s
                """
                cursor.execute(query, (login_id, limit))
                return cursor.fetchall()
        except Error as error:
            print(f"BMI records find error: {error}")
            return []

    def close(self):
        if self.connection:
            self.connection.close()
            print("MariaDB connection closed.")
