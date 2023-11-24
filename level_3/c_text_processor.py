"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text: str):
        self.text = text

    def to_upper(self) -> str:
        return self.text.upper()

    def summarize(self) -> str:
        return f'Total text length: {len(self.text)}'
    

class AdvancedTextProcessor(TextProcessor):
    def summarize(self) -> str:
        response = super().summarize()
        response += f', total number of words in the text: {len(self.text.split())}'
        return response


if __name__ == '__main__':
    old_processor = TextProcessor(
        "Power is when we have every justification to kill, and we don't")
    new_processor = AdvancedTextProcessor(
        'My mama always said life was like a box of chocolates. You never know what gonna get')
    
    print(old_processor.to_upper())
    print(old_processor.summarize())
    print()
    print(new_processor.to_upper())
    print(new_processor.summarize())
