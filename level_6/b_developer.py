"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса ItDepartmentEmployee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом,
       чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self) -> str:
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float):
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, employee: Employee, amount: float) -> None:
        employee.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, employee: Employee, amount: float) -> None:
        employee.salary -= amount


class Developer(SuperAdminMixin, ItDepartmentEmployee):
    def __init__(
        self,
        name: str,
        surname: str,
        age: int,
        salary: float,
        programming_language: str,
    ) -> None:
        super().__init__(name, surname, age, salary)
        self.programming_language = programming_language

    def get_info(self) -> str:
        return super().get_info() + f'. Writes code in {self.programming_language}'


if __name__ == '__main__':
    john_doe = Developer('John', 'Doe', 58, 500.00, '1C')
    print(john_doe.get_info())
    john_doe.increase_salary(john_doe, 1000.00)
    print(john_doe.get_info())
    john_doe.decrease_salary(john_doe, 1500.00)
    print(john_doe.get_info())
