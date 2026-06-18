from models.bmi_model import BMIRecordModel


class HistoryService:
    """Business logic for BMI history."""

    def __init__(self, database):
        self.bmi_record_model = BMIRecordModel(database)

    def get_recent_records(self, limit=10):
        return self.bmi_record_model.get_recent_records(limit)

    def delete_record(self, record_id):
        if record_id <= 0:
            return False

        return self.bmi_record_model.delete_record(record_id)
