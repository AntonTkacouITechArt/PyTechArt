import unittest

from topic2.task1 import Department


class Test_task_2_1(unittest.TestCase):
    def test_get_budget_1(self):
        result = Department("company_1", {"staff_1":2000, "staff_2":1000, "staff_3":0, "staff_4":3000 }, 7000 )
        self.assertEqual(result.get_budget_plan(), 1000)

    def test_get_budget_2(self):
        result = Department("company_1", {"staff_1":100000, "staff_2":0, "staff_3":2000, "staff_4":5000 }, 7000 )
        self.assertRaises(Department.BudgetError, result.get_budget_plan)

    def test_department_BudgetError(self):
        self.assertTrue(issubclass(Department.BudgetError, ValueError))

    def test_average_salary_float(self):
        result = Department("company_1", {"staff_1":2000, "staff_2":0, "staff_3":0, "staff_4":0 }, 7000 )
        self.assertTrue(isinstance(result.average_salary, float))

    def test_average_salary_round_1(self):
        result = Department("company_1", {"staff_1":0, "staff_2":0, "staff_3":0, "staff_4":0 }, 7000 )
        self.assertEqual(result.average_salary, 0.00)

    def test_average_salary_round_2(self):
        result = Department("company_1", {"staff_1":2000, "staff_2":0, "staff_3":0, "staff_4":0 }, 7000 )
        self.assertEqual(result.average_salary, 500.00)

    def test_average_salary_round_3(self):
        result = Department("company_1", {"staff_1":7.372, "staff_2":0, "staff_3":0, "staff_4":0 }, 7000 )
        self.assertEqual(result.average_salary, 1.84)

    def test_average_salary_round_4(self):
        result = Department("company_1", {"staff_1":10.22, "staff_2":0, "staff_3":0, "staff_4":0 }, 7000 )
        self.assertEqual(result.average_salary, 2.56)

    # def test_average_salary_property(self):
    #     result = Department("company_1", {"staff_1":7.372, "staff_2":0, "staff_3":0, "staff_4":0 }, 7000 )
    #     self.assertEqual(result.average_salary, 1.84)

    def test_merge_departments(self):
        data1 = {
            'Anton': 400,
            'Nikita': 5000,
            'Egor': 5000
        }
        data2 = {
            'Sasha': 3000,
            'Dima': 10000,
            'Peter': 2500,
        }
        a = Department('ITechArt', data1, 20000)
        b = Department('ITechArt1', data1, 32000)
        c = Department('ITechAr', data1, 32000)
        d = Department('NoName', data2, 20000)
        f = Department('And', data2, 20000)
        e = Department.merge_departments(a, b, c, d, f)
        self.assertEqual(e.name, "And - ITechAr - ITechArt - ITechArt1 - NoName")
        self.assertEqual(len(e.employees), 6)
        self.assertEqual(e.budget, 124000)

    def test_dunder_method_add(self):
        data1 = {
            'Anton': 400,
            'Nikita': 5000,
            'Egor': 5000
        }
        data2 = {
            'Sasha': 3000,
            'Dima': 10000,
            'Peter': 2500,
        }
        a = Department('ITechArt', data1, 20000)
        b = Department('ITechArt1', data2, 32000)
        c = a + b
        self.assertEqual(c.name, "ITechArt - ITechArt1")
        self.assertEqual(len(c.employees), 6)
        self.assertEqual(c.budget, 52000)

    def test_dunder_method_str(self):
        data1 = {
            'Anton': 400,
            'Nikita': 5000,
            'Egor': 5000
        }
        data2 = {
            'Sasha': 3000,
            'Dima': 10000,
            'Peter': 2500,
        }
        a = Department('ITechArt', data1, 20000)
        b = Department('ITechArt1', data2, 32000)
        c = a + b
        self.assertEqual(str(c), "ITechArt - ITechArt1 (6 - 4316.67, 52000)")

    def test_dunder_method_or_1(self):
        data1 = {
            'Anton': 400,
            'Nikita': 5000,
            'Egor': 5000
        }
        data2 = {
            'Sasha': 3000,
            'Dima': 10000,
            'Peter': 2500,
        }
        a = Department('ITechArt', data1, 0)
        b = Department('ITechArt1', data2, 32000)
        self.assertRaises(Department.BudgetError, lambda : a|b)
        
    def test_dunder_method_or_2(self):
        data1 = {
            'Anton': 100,
            'Nikita': 100,
            'Egor': 100,
        }
        data2 = {
            'Sasha': 3000,
            'Dima': 10000,
            'Peter': 10000,
        }
        a = Department('ITechArt', data1, 20000)
        b = Department('ITechArt1', data2, 32000)
        c = a | b
        self.assertTrue(c==a)

    def test_dunder_method_or_3(self):
        data1 = {
            'Anton': 100,
            'Nikita': 100,
            'Egor': 100,
        }
        a = Department('ITechArt', data1, 20000)
        b = Department('ITechArt1', data1, 20000)
        c = a | b
        self.assertTrue(c==a)


if __name__ == '__main__':
    unittest.main()
