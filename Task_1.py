import doctest
from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов


class Wall:
    def __init__(self, length: Union[int, float], width: Union[int, float], height: Union[int, float]) -> None:
        """

        :param length: Длина стены в мм
        :param width: Толщина стены в мм
        :param height: Высота стены в мм

        Пример:
        >>> wall = Wall(1000, 250, 3300)  # инициализация экземпляра класса Wall
        """
        if not isinstance(length, (int, float)):
            raise TypeError('Длина стены должна иметь тип данных int или float')
        if length <= 0:
            raise ValueError('Длина стены должна быть больше 0')
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError('Толщина стены должна иметь тип данных int или float')
        if width < 0:
            raise ValueError('Толщина стены должна быть больше 0')
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError('Высота стены должна иметь тип данных int или float')
        if height < 0:
            raise ValueError('Высота стены должна быть больше 0')
        self.height = height

    def change_length(self, new_length):  # метод изменения длины стены
        ...

    def rotate(self, degrees):  # метод вращения стены
        ...


class Human:
    def __init__(self, age: int, name: str) -> None:
        """

        :param age: Возраст человека
        :param name: Имя человека

        Пример:
        >>> human = Human(45, 'John')  # инициализация экземпляра класса Human
        """

        if not isinstance(age, int):
            raise TypeError('Возраст должен иметь тип данных int')
        if age < 0:
            raise ValueError('Возраст не может быть отрицательным')
        self.age = age

        if not isinstance(name, str):
            raise TypeError('Имя должно иметь тип данных str')
        self.name = name

    def set_specialty(self):  # метод назначения специальности для человека
        ...

    def get_birthplace(self):  # метод получения места рождения человека
        ...


class File:
    def __init__(self, name: str, size: int) -> None:
        """

        :param name: Имя файла
        :param size: Размер файла

        Пример:
        >>> file = File('Test', 1024)  # инициализация экземпляра класса File
        """
        if not isinstance(name, str):
            raise TypeError('Имя файла должно иметь тип данных str')
        self.name = name  # имя файла

        if not isinstance(size, int):
            raise TypeError('Размер файла должен иметь тип данных int')
        if size < 0:
            raise ValueError('Размер файла не может быть отрицательным')
        self.size = size  # размер файла

    def rename(self, new_name: str):  # метод для переименовывания файла
        if not isinstance(new_name, str):
            raise TypeError('Новое имя должно иметь тип данных str')
        if self.name == new_name:
            raise ValueError('Новое имя не должно быть таким же, как старое')
        self.name = new_name



if __name__ == "__main__":
     # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
