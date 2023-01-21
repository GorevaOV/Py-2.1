import doctest

class Hamster:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Хомяк"
        :param name: Имя хомяка
        :param age: Возраст Хомяка
        Примеры:
        >>> Bob = Hamster("Bob", 2)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя хомяка может быть только строкой")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст собаки должен быть целочисленным")
        if age < 0:
            raise ValueError("Возраст хомяка не может быть отрицательным")
        if age > 3:
            raise ValueError("Проверьте хомяка =(")
        self.age = age

    def feed(self) -> str:
        """
        Покормить хомяка
        :return: "self.name" кушает
        Примеры:
        >>> Bob = Hamster("Bob", 2)
        >>> Bob.feed()
        """
        ...

    def bury(self, hamster_age: int) -> bool:
        """
        R.I.P
        :return: "Он теперь в лучшем мире"
        Примеры:
        >>> Bob = Hamster("Bob", 3)
        >>> Bob.bury(4)
        """
        if not isinstance(hamster_age, int):
            raise TypeError("Возраст хомяка может быть только целочисленным")
        if hamster_age <= 3:
            raise ValueError("Верните хомяка на место, он просто спит")
        ...


class Bag:
    def __init__(self, capacity: int, occupied: int):
        """
        Создание и подготовка к работе объекта "Рюкзак"
        :param capacity: Объем рюкзака
        :param occupied: Занятый объём рюкзака
        Примеры:
        >>> bag = Bag(5, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Объем рюкзака должен быть численным")
        if capacity <= 0:
            raise ValueError("Объем рюкзака не может быть отрицательным")
        self.capacity = capacity

        if not isinstance(occupied, (int, float)):
            raise TypeError("Занимаемый объем рюкзака должен быть численным")
        if occupied < 0:
            raise ValueError("Занимаемый объем рюкзака не может быть отрицательным")
        self.occupied = occupied


    def add_sandwich_to_bag(self, sandwich: int) -> None:
        """
        Добавление сендвича в рюкзак.
        :param sandwich: Количество добавляемых сендвичей
        :raise ValueError: Если количество добавляемых сендвичей больше объема рюкзака
        Примеры:
        >>> bag = Bag(5, 0)
        >>> bag.add_sandwich_to_bag(2)
        """
        if not isinstance(sandwich, int):
            raise TypeError("Количество сендвичей должно быть целым")
        if sandwich < 0:
            raise ValueError("Количество сендвичей не может быть отрицательным")
        ...

    def remove_sandwich_from_bag(self, sandwich: int) -> int:
        """
        Извлечение чего либо из коробки
        :param sandwich: Количество извлекаемых сендвичей
        :raise ValueError: Если количество извлекаемых сендвичей превышает количество сендвичей в рюкзаке,
        то возвращается ошибка.
        :return: Количество реально извлеченных сендвичей
        Примеры:
        >>> bag = Bag(5, 5)
        >>> bag.remove_sandwich_from_bag(200)
        """
        ...


class Bicycle:
    def __init__(self, color: str, owner: str):
        """
        Создание и подготовка к работе объекта "Велосипед"
        :param color: Цвет велосипеда
        :param owner: Владелец велосипеда
        Примеры:
        >>> bike = Bicycle("Black", "Billy")  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет велосипеда может быть только строкой")
        self.color = color
        if not isinstance(owner, str):
            raise TypeError("Владелец велосипеда может быть только строкой")
        self.owner = owner

    def sit_cycle(self) -> bool:
        """
        Сесть на велосипед
        Примеры:
        >>> bike = Bicycle("Black", "Billy")
        >>> bike.sit_cycle()
        """
        ...

    def ride_cycle(self) -> bool:
        """
        Поехать на велосипеде
        Примеры:
        >>> bike = Bicycle("Black", "Billy")
        >>> bike.ride_cycle()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации