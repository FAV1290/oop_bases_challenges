"""
У нас есть класс банковского аккаунта со свойствами: полное имя владельца и баланс, но не реализован
метод, который увеличивает баланс.

Задания:
    1. Допишите логику в метод increase_balance,
    который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечатайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float) -> None:
        if income > 0:
            self.balance += income
        else:
            raise ValueError('Income should have positive value')


if __name__ == '__main__':
    user_account = BankAccount('John Doe', 10000.0)
    print('Balance before:', user_account.balance)
    user_account.increase_balance(1000.5)
    print('Balance after:', user_account.balance)
