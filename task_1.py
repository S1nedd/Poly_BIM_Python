class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Конструктор экземпляра класса Book

        :param name: Имя книги
        :param author: Автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self):
        return self._author

    """
    так как в дочерних классах атрибуты "name" и "author" будут унаследованы,
    то метод __str__ можно так же наследовать
    """
    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    """
    в дочерних классах есть уникальные дополнительные атрибуты, необходимые для конструктора, поэтому метод __repr__
    будет перегружен в каждый дочерний класс
    """
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        """
        Конструктор экземпляра класса PaperBook

        :param name: Имя книги
        :param author: Автор книги
        :param pages: Количество страниц книги
        """
        super().__init__(name, author)  # наследуем атрибуты name и author у базового класса Book

        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц книги."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц у книги."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        Конструктор экземпляра класса AudioBook

        :param name: Имя книги
        :param author: Автор книги
        :param duration: Продолжительность книги
        """
        super().__init__(name, author)  # наследуем атрибуты name и author у базового класса Book

        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность книги."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает продолжительность книги."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть положительной")
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"
