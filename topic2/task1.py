import typing
class Department:
    """Class Department vars:budget(int), employees(Dict[str, float]), name(str)
    methods:get_budget_plan(float), average_salary(float),
    merge_departments(Department) """
    class BudgetError(ValueError):
        """Budget below zero"""

    def __init__(self, name: typing.Optional[str],
                 employees: typing.Dict[str, float],
                 budget: typing.Optional[int]):
        self.budget = budget
        self.employees = employees
        self.name = name

    def __str__(self):
        return '{} ({} - {}, {})'.format(self.name, len(self.employees),
                                         self.average_salary, self.budget)

    def __or__(self, other: 'Department') -> 'Department':
        a = self.get_budget_plan()
        b = other.get_budget_plan()
        if a >= b:
            return self
        else:
            return other

    def __add__(self, other: 'Department') -> 'Department':
        return Department.merge_departments([self,other])


    def get_budget_plan(self) -> float:
        """Return budget_plan(float) = all_budget - all_salary"""
        department_budget = self.budget - sum(self.employees.values())
        if department_budget < 0:
            raise Department.BudgetError("""the
            department has a negative budget""")
        return department_budget

    @property
    def average_salary(self) -> float:
        """Return avg_salary(float) rounding to 2"""
        return round(sum(self.employees.values()) / len(self.employees), 2)

    @classmethod
    def merge_departments(cls, *departments: 'Department') -> 'Department':
        """Merge 2 or more departments -> 1 department"""
        all_budget = sum(department.budget for department in departments)
        employees = {k:v for department in departments
                        for k,v in department.employees.items()}
        sorted_list = ((department.average_salary, department.name)
                        for department in departments)
        sorted_list = sorted(sorted_list, key=lambda i: i[0], reverse=True)
        sorted_list = sorted(sorted_list, key=lambda i: i[1])
        name = ' - '.join((other_name[1] for other_name in sorted_list))
        temp = Department(name, employees, all_budget)
        _ = temp.get_budget_plan() # check raise
        return temp


if __name__ == '__main__':
    data1 = {
        'Anton':400,
        'Nikita':5000,
        'Egor':5000
    }
    data2 = {
        'Sasha':3000,
        'Dima':10000,
        'Peter':2500,
    }
    a = Department('ITechArt',data1,20000)
    b = Department('ITechArt1',data1,32000)
    c = Department('ITechAr',data1,32000)
    d = Department('NoName', data2,20000)
    f = Department('And', data2, 20000)
    e = Department.merge_departments(a,b,c,d,f)
    print(e)
