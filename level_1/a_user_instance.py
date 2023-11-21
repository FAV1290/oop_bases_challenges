"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде:
    Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    def render_user_info_str(user: User) -> str:
        age_str = f'{user.age} year{"s" * (user.age != 1)}'
        return f'User info: {user.name}, {user.username}, {age_str}, {user.phone}.'

    current_user = User('John Doe', 'johndoe815', 32, '+1 (234) 567-89-00')
    print(render_user_info_str(current_user))
