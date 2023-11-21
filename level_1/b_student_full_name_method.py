"""
Задания:
    1. Cоздайте экземпляр класса студенда.
    2. Получите его полное имя используя метод get_full_name.
    3. Положите результат вызова метода get_full_name в переменную и распечатайте ее.
"""


class Student:
    def __init__(self, name: str, surname: str, faculty: str, course: int):
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.course = course

    def get_full_name(self) -> str:
        return f"Student's full name: {self.surname}, {self.name}"


if __name__ == '__main__':
    new_student = Student('John', 'Doe', 'Faculty of Mathematics', 1)
    new_student_full_name = new_student.get_full_name()
    print(new_student_full_name)
