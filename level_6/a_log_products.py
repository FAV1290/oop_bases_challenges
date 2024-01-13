"""
У нас есть различные типы классы для различных типов продуктов.
Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь,
       что вызовы логируются.
"""


class PrintLoggerMixin():
    @staticmethod
    def log(message: str) -> None:
        print(message)


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self) -> str:
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self) -> None:
        self.price *= 1.2
        logger_message = f'INFO: {self.title} turned even more premium. '\
                         f'New price: {"{:.2f}".format(self.price)}'
        self.log(logger_message)

    def get_info(self) -> str:
        base_info = super().get_info()
        self.log(f'INFO: {self.title} info has been requested')
        return f'{base_info} (Premium)'


class DiscountedProduct(PrintLoggerMixin, Product):
    def decrease_price(self) -> None:
        self.price /= 1.2
        logger_message = f'INFO: {self.title} turned more far from chicken eggs.'\
                         f'New price: {"{:.2f}".format(self.price)}'
        self.log(logger_message)

    def get_info(self) -> str:
        base_info = super().get_info()
        self.log(f'INFO: {self.title} info has been requested')
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    chicken_eggs = PremiumProduct('Chicken eggs', 99999999.99)
    chicken_eggs.increase_price()
    chicken_eggs_info = chicken_eggs.get_info()
    black_caviar = DiscountedProduct('Black caviar', 999.99)
    black_caviar.decrease_price()
    black_caviar_info = black_caviar.get_info()
