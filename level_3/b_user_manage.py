"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    usernames = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> None:
        return self.usernames
    
    def show_features(self, username_to_add: str) -> None:
        print(f'Current users: {self.get_users()}')
        self.add_user(username_to_add)
        print(f'User with username {username_to_add} has been added')
        print(f'Current users: {self.get_users()}')


class AdminManager(UserManager):
    def ban_username(self, username: str) -> str:
        try:
            self.usernames.remove(username)
            return f'User with username {username} has been banned'
        except ValueError:
            return f'User with username {username} was not found'
        
    def show_features(self, username_to_add: str, usernames_to_ban: list[str]) -> None:
        super().show_features(username_to_add)
        for username in usernames_to_ban:
            ban_feedback = self.ban_username(username)
            print(ban_feedback)
        print(f'Current users: {self.get_users()}')


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()

    def show_features(self, username_to_add: str, usernames_to_ban: list[str]) -> None:
        super().show_features(username_to_add, usernames_to_ban)
        self.ban_all_users()
        print('Apocalypse now! All users have been banned')
        print(f'Current users: {self.get_users()}')


if __name__ == '__main__':
    user_manager = UserManager()
    admin_manager = AdminManager()
    super_admin_manager = SuperAdminManager()

    user_manager.show_features('victoria259')
    print()
    admin_manager.show_features('joe123', ['alex444', 'joe123'])
    print()
    super_admin_manager.show_features('maria012', ['robert349', 'maria012'])
