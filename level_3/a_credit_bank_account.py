"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> None:
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        self.balance -= amount

    def print_balance(self) -> None:
        print(self.balance)


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    my_bank_account = BankAccount('John Doe', 500.00)
    my_credit_account = CreditAccount('John Doe', 500.00)

    my_bank_account.print_balance()
    my_bank_account.increase_balance(500.00)
    my_bank_account.decrease_balance(400.00)
    my_bank_account.print_balance()
    print()
    my_credit_account.print_balance()
    my_credit_account.increase_balance(500.00)
    my_credit_account.decrease_balance(400.00)
    my_credit_account.print_balance()
    print(my_credit_account.is_eligible_for_credit())
    my_credit_account.increase_balance(400.01)
    print(my_credit_account.is_eligible_for_credit())



