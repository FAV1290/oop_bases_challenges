"""
Задания:
    1. Запустите текущий код и посмотрите на вывод.
    2. Допишите класс User таким образом, чтобы при вызове print() на его инстансах появлялась информация
       об айдишнике пользователя и его емэйле, а при вызове repr() возвращалась информация о том,
       является ли пользователь админом
"""


class User:
    def __init__(self, user_id: int, email: str, is_admin: bool):
        self.user_id = user_id
        self.email = email
        self.is_admin = is_admin

    def __str__(self) -> str:
        return f'User with id {self.user_id} and e-mail {self.email}'

    def __repr__(self) -> str:
        first_word = 'Admin' if self.is_admin else 'Non-admin'
        return f'<{first_word} User object at 0x00000{hex(id(self)).upper()[2:]}>'


if __name__ == '__main__':
    user_instance = User(user_id=3, email='dev@yandex.ru', is_admin=True)
    print(user_instance)
    print(repr(user_instance))
