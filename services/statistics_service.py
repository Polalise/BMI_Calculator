class StatisticsService:
    """Builds BMI statistics view data from stored BMI records."""

    CATEGORY_ORDER = ["저체중", "정상", "과체중", "비만", "고도비만"]

    def __init__(self, db):
        self.db = db

    def get_statistics(self):
        statistics = self.db.get_bmi_statistics()
        summary = statistics.get("summary") or {}
        total_count = summary.get("total_count") or 0
        categories = statistics.get("categories") or []

        return {
            "summary": {
                "total_count": total_count,
                "average_bmi": summary.get("average_bmi"),
                "min_bmi": summary.get("min_bmi"),
                "max_bmi": summary.get("max_bmi"),
                "average_weight": summary.get("average_weight"),
                "average_height": summary.get("average_height"),
            },
            "categories": self._build_category_rows(categories, total_count),
            "latest_record": statistics.get("latest_record"),
            "has_data": total_count > 0,
        }

    def _build_category_rows(self, categories, total_count):
        counts_by_category = {
            row.get("category"): row.get("count", 0)
            for row in categories
        }
        ordered_categories = [
            category for category in self.CATEGORY_ORDER if category in counts_by_category
        ]
        extra_categories = sorted(
            category for category in counts_by_category if category not in self.CATEGORY_ORDER
        )

        rows = []
        for category in ordered_categories + extra_categories:
            count = counts_by_category[category]
            percentage = round((count / total_count) * 100, 1) if total_count else 0
            rows.append(
                {
                    "category": category,
                    "count": count,
                    "percentage": percentage,
                }
            )

        return rows
