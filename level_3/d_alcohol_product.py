"""
У нас есть класс Product, который содержит в себе информацию о продукте.
Еще у нас есть класс AlcoholProduct, но метод is_available для него не подходит, так как
алкоголь нельзя продавать с 5 утра до 11 вечера

Задания:
    1. Переопределите метод is_available в классе AlcoholProduct с использованием super()
    2. is_available у AlcoholProduct должен возвращать False если сейчас часы между 5 утра и 11 вечера.
       Для определения текущего часа можно использовать datetime.now().hour
    3. Создайте экземпляр класса AlcoholProduct и проверьте, можно ли сейчас продавать алкоголь.
"""
from datetime import datetime


class Product:
    def __init__(self, title: str, price: float, stock_quantity: int):
        self.title = title
        self.price = price
        self.stock_quantity = stock_quantity

    def get_discounted_price(self, discount_percentage: int) -> float:
        return self.price * (1 - discount_percentage / 100)

    def is_available(self) -> bool:
        return self.stock_quantity > 0


class AlcoholProduct(Product):
    def is_available(self) -> bool:
        allowed_for_booze_hours = list(range(5)) + [23]
        return super().is_available() and datetime.now().hour in allowed_for_booze_hours


if __name__ == '__main__':
    jack_daniels = AlcoholProduct("Jack Daniel's Tennessee Honey", 29.90, 5)
    print(jack_daniels.is_available())
