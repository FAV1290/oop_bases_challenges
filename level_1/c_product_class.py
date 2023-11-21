"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде:
    Информация о продукте: название, описание, цена, вес
"""
from decimal import Decimal


class Product:
    def __init__(self, name: str, description: str, price_usd: Decimal, weight_grams: int):
        self.name = name
        self.descr = description
        self.price_usd = price_usd
        self.weight_grams = weight_grams

    def __str__(self) -> str:
        if len(self.descr) > 50:
            return '\n'.join([
                f'Product info: {self.name}, {self.price_usd} USD, {self.weight_grams} g.',
                f'Product description: {self.descr}',
            ])
        else:
            return ''.join([
                f'Product info: {self.name}, {self.descr}, ',
                f'{self.price_usd} USD, {self.weight_grams} g.',
            ])


if __name__ == '__main__':
    first_product = Product(
        name='Milk',
        description="whole pasteurized cow's milk (3.25 milkfat)",
        price_usd=Decimal('1.49'),
        weight_grams=1000,
    )
    second_product = Product(
        name='Heavy Whipping Cream',
        description='With just two ingredients, '
                    'it gives your soups and sauces the consistency they need, '
                    'so your meals can reach their full potential of deliciousness',
        price_usd=Decimal('4.58'),
        weight_grams=946,
    )
    print(first_product)
    print()
    print(second_product)
