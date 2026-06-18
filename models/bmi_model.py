from pymysql import Error


class BMIRecordModel:
    """DB access for BMI record history."""

    def __init__(self, database):
        self.database = database

    def get_recent_records(self, member_id, limit=10):
        return self.database.get_bmi_records(member_id, limit)

    def delete_record(self, record_id, member_id):
        if self.database.connection is None:
            print("Database connection is not available.")
            return False

        try:
            with self.database.connection.cursor() as cursor:
                query = "DELETE FROM bmi_records WHERE id = %s AND member_id = %s"
                cursor.execute(query, (record_id, member_id))
                deleted_count = cursor.rowcount

            self.database.connection.commit()
            return deleted_count > 0
        except Error as error:
            print(f"BMI record delete error: {error}")
            return False
