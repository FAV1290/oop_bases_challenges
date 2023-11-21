"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса
       и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float) -> None:
        if income >= 0:
            self.balance += income
        else:
            raise ValueError('Income should have positive value')

    def decrease_balance(self, expense: float) -> None:
        if expense < 0:
            raise ValueError('Expense should have positive value')
        elif self.balance - expense < 0:
            raise ValueError('Insufficient funds')
        else:
            self.balance -= expense


if __name__ == '__main__':
    user_account = BankAccount('John Doe', 10000.0)
    print('Balance before:', user_account.balance)
    user_account.decrease_balance(1000.0)
    print('Balance after:', user_account.balance)
    try:
        user_account.decrease_balance(10000.0)
    except ValueError:
        print("We've got ValueError")
        print('Сurrent balance:', user_account.balance)
