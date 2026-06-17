class BMICalculator:
    """BMI 계산과 판정 로직을 담당합니다."""

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height / 100

    def calculate_bmi(self):
        return self.weight / (self.height**2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "저체중"
        if bmi < 23:
            return "정상"
        if bmi < 25:
            return "과체중"
        if bmi < 30:
            return "비만"
        return "고도비만"

    def get_result(self):
        bmi = self.calculate_bmi()

        return {
            "bmi": round(bmi, 2),
            "category": self.get_bmi_category(),
        }
