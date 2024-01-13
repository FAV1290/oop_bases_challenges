"""
Банк позволяет уходить в минус по счету, чтобы клиенты не оказывались в без денег в самый неподходящий момент

Задания:
    1. Напишите логику метода decrease_balance таким образом, чтобы можно было уменьшать баланс,
       но чтобы он не становился меньше чем значение в атрибуте класса min_balance.
       Если он будет меньше - вызывайте исключение ValueError
    2. Создайте экземпляр класса BankAccount, вызовите у него метод decrease_balance и убедитесь, что баланс уменьшается
       и если он уменьшается больше чем можно, то вызывается исключение
"""


class BankAccount:
    min_balance = -100

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def decrease_balance(self, amount: float) -> None:
        new_balance = self.balance - amount
        if new_balance >= self.min_balance:
            self.balance = new_balance
        else:
            raise ValueError(
                f"{self.owner}'s transaction was declined due to overdraft limit exceedance")


if __name__ == '__main__':
    john_doe_account = BankAccount('John Doe', 150.0)
    print(john_doe_account.balance)
    john_doe_account.decrease_balance(150)
    print(john_doe_account.balance)
    john_doe_account.decrease_balance(101)
