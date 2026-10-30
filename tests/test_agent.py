import unittest
import pandas as pd

from tools.student_risk import analyze_students


class TestStudentRisk(unittest.TestCase):

    def setUp(self):
        self.students = pd.DataFrame({
            "student_id": ["S001", "S002", "S003"],
            "student_name": ["Student A", "Student B", "Student C"],
            "attendance": [42, 75, 95],
            "marks": [35, 65, 90],
            "assignments": [30, 70, 95]
        })

    def test_analysis_returns_results(self):
        results = analyze_students(self.students)
        self.assertIsNotNone(results)

    def test_high_risk_student(self):
        results = analyze_students(self.students)
        self.assertIn("High", str(results))

    def test_student_data_is_not_empty(self):
        self.assertFalse(self.students.empty)

    def test_attendance_range(self):
        self.assertTrue(
            self.students["attendance"].between(0, 100).all()
        )

    def test_marks_range(self):
        self.assertTrue(
            self.students["marks"].between(0, 100).all()
        )

    def test_assignments_range(self):
        self.assertTrue(
            self.students["assignments"].between(0, 100).all()
        )


if __name__ == "__main__":
    unittest.main()
