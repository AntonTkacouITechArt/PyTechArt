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
        budget = self.budget + other.budget
        employees = {**self.employees, **other.employees}

        if self.average_salary > other.average_salary:
            name = self.name + ' - ' + other.name
        elif self.average_salary == other.average_salary:
            if self.name >= other.name:
                name = self.name + ' - ' + other.name
            else:
                name = other.name + ' - ' + self.name
        else:
            name = other.name + ' - ' + self.name

        temp = Department(name, employees, budget)
        _ = temp.get_budget_plan()
        return temp

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
        all_budget = 0
        name = ''
        employees = {}
        sorted_list = []
        for department in departments:
            all_budget += department.budget
            employees.update(department.employees)
            sorted_list.append(
                tuple([department.average_salary, department.name]))
        sorted_list = sorted(sorted_list, key=lambda i: i[0], reverse=True)
        sorted_list = sorted(sorted_list, key=lambda i: i[1])
        for other_name in sorted_list:
            name += other_name[1]
            if sorted_list[-1][1] != other_name[1]:
                name += ' - '

        temp = Department(name, employees, all_budget)
        _ = temp.get_budget_plan()
        return temp
