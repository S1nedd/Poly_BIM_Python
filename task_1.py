class Human:
    """ Базовый класс человека. """
    def __init__(self, name: str, age: int, gender: str, birthplace: str):
        """
        Конструктор экземпляра класса Human
        :param name: Имя человека
        :param age: Возраст человека
        :param gender: Пол человека
        :param birthplace: Место рождения человека
        """
        if not isinstance(name, str):
            raise TypeError('Имя должно быть типа str')
        self._name = name

        if not isinstance(age, int):
            raise TypeError('Возраст должен быть типа int')
        if age <= 0:
            raise ValueError('Возраст должен быть положительным')
        self._age = age

        if not isinstance(gender, str):
            raise TypeError('Пол должен быть типа str')
        self._gender = gender

        if not isinstance(birthplace, str):
            raise TypeError('Место рождения должно быть типа str')
        self._birthplace = birthplace

        self._coordinates = [0, 0]  # положение человека в пространстве

    def __str__(self) -> str:
        return f'Hi, my name is {self._name}\n' \
        f'I am {self._age} years old\n' \
        f'I was born in {self._birthplace}\n'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r}, age={self._age}, gender={self._gender!r}, birthplace={self._birthplace!r})'

    def move(self, x: int, y: int):
        """
        Метод перемещения человека
        :param x: Координата x
        :param y: Координата y
        """
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError('Координаты должны быть типа int')
        self._coordinates[0] += x
        self._coordinates[1] += y

    def sing(self) -> str:
        """
        Метод, исполняющий припев песни
        """
        return f'{self._name} sings:\n' \
        'Never gonna give you up\n' \
        'Never gonna let you down\n' \
        'Never gonna make you cry\n' \
        'Never gonna run around and desert you\n' \
        'Never gonna say goodbye\n' \
        'Never gonna tell a lie and hurt you'


class Sportsman(Human):
    """ Дочерний класс Sportsman. """
    def __init__(self, name, age, gender, birthplace, specialty: str):
        """
        Конструктор экземпляра класса Sportsman
        :param name: Имя спортсмена
        :param age: Возраст спортсмена
        :param gender: Пол спортсмена
        :param birthplace: Место рождения спортсмена
        :param specialty: Специальность спортсмена
        """
        super().__init__(name, age, gender, birthplace)  # наследование атрибутов у базового класса

        self._specialty = specialty

    @property
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, value):
        if not isinstance(value, str):
            raise TypeError('Специальность должна быть типа str')
        self._specialty = value

    def __str__(self):  # перегружаем метод __str__ так как у класса Pilot есть дополнительный атрибут
        human_say = super().__str__()
        return human_say + f'My specialty is {self._specialty}'

    def __repr__(self):  # перегружаем метод __repr__ так как у класса Pilot есть дополнительный атрибут
        human_repr = super().__repr__()
        return human_repr[:-1] + f', specialty={self._specialty!r})'

    def move(self, x: int, y: int):  # перегружаем метод move, так как у спортсмена физ. подготовка лучше, поэтому передвигается он дальше)
        self._coordinates[0] += 2 + x
        self._coordinates[1] += 2 + y


if __name__ == "__main__":
    # Write your solution here

    vasya = Human('Vasya', 25, 'Male', 'Russia')

    print(vasya)
    print(repr(vasya))
    print('\n')
    print(vasya._coordinates)
    vasya.move(1, 5)
    print(vasya._coordinates)
    print('\n')
    print(vasya.sing())

    anna = Sportsman('Anna', 30, 'Female', 'Belarus', 'Jumper')

    print(anna)
    print(repr(anna))
    print('\n')
    print(anna.specialty)
    print(anna._coordinates)
    anna.move(3, 8)
    print(anna._coordinates)
    print('\n')
    print(anna.sing())
