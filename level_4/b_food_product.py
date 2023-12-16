"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так,
       чтобы там хранилось еще свойство expiration_date. Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info,
       чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct,
       чтобы там учитывался еще и срок годности. Если он меньше чем текущая дата -
       то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""
from datetime import datetime


class Product:
    def __init__(self, title: str, quantity: int):
        self.title = title
        self.quantity = quantity

    def get_full_info(self) -> str:
        return f'Product {self.title}, {self.quantity} in stock.'

    def is_available(self) -> bool:
        return self.quantity > 0


class FoodProduct(Product):
    def __init__(self, title: str, quantity: int, expiration_date: datetime):
        super().__init__(title, quantity)
        self.expiration_date = expiration_date

    def get_full_info(self) -> str:
        expires_at = self.expiration_date.strftime("%d.%m.%Y")
        return f'Product {self.title}, expires at {expires_at}, {self.quantity} in stock.'

    def is_available(self, dates_only: bool = True) -> bool:
        if not super().is_available():
            return False
        elif dates_only:
            return self.expiration_date.date() >= datetime.now().date()
        else:
            return self.expiration_date >= datetime.now()


if __name__ == '__main__':
    lamp = Product('Table lamp', 0)
    milk = FoodProduct('Prostokvashino 3,2% 1L', 50, datetime.now())

    for product in [lamp, milk]:
        print(product.get_full_info())
        print('Available now') if product.is_available() else print('Out of stock')
        print()
