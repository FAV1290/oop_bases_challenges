"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь.
       Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей.
       Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import os
import csv
import json
from typing import TypeAlias, Any


class FileHandler:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> Any:
        with open(self.filename, 'r') as file_handler:
            return file_handler.read()

    def __str__(self) -> str:
        return str(self.read()) if isinstance(self.read(), str) else self.__repr__()


class JSONDumpsStrMixin:
    def read(self) -> Any: ...

    def __str__(self) -> str:
        return json.dumps(self.read(), sort_keys=True, indent=4)


class JSONHandler(JSONDumpsStrMixin, FileHandler):
    JSON: TypeAlias = dict[str, 'JSON'] | list['JSON'] | str | int | float | bool | None

    def read(self) -> JSON:
        with open(self.filename, 'r') as file_handler:
            result: JSONHandler.JSON = json.load(file_handler)
            return result


class CSVHandler(JSONDumpsStrMixin, FileHandler):
    def read(self, delimiter: str = ',') -> list[dict[str, str]]:
        reader = csv.reader(open(self.filename, 'r'), delimiter=delimiter)
        csv_records = []
        headers: list[str] = []
        for row in reader:
            if headers:
                row_dict = {}
                for index in range(len(headers)):
                    row_dict[headers[index]] = row[index]
                csv_records.append(row_dict)
            else:
                headers = row
        return csv_records


if __name__ == '__main__':
    text_handler = FileHandler('level_4/data/text.txt')
    json_handler = JSONHandler('level_4/data/recipes.json')
    csv_handler = CSVHandler('level_4/data/user_info.csv')

    for handler in [text_handler, json_handler, csv_handler]:
        assert isinstance(handler, FileHandler)
        print(handler)
        input('\nPress enter to continue...')
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
