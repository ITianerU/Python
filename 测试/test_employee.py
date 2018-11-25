from unittest import TestCase
from Employee import Employee

class TestEmpoyee(TestCase):
    def setUp(self):
        self.emp = Employee("老", "王", 100000)

    def test_give_default_salary(self):
        res = self.emp.give_raise()
        self.assertEqual(105000, res)

    def test_give_custom_salary(self):
        res = self.emp.give_raise(50000)
        self.assertEqual(150000, res)