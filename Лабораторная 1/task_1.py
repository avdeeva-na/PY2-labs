import doctest
from typing import Union
class Friend:
    """
    Документация на класс.
    Класс описывает список друзей
    """
    def __init__(self, number:int, name:str, age:int, country:str):
        """ Создание и подготовка к работе объекта "Друзья"
        :param number: Количество друзей
        :param name: Имена друзей
        :param age: Возраст друзей
        :param country: Страна нахождения друзей
        Примеры:
        >>> friend = Friend(3,"Mike", 25, "USA")
        """
        self.number = None
        self.init_number(number)
        self.age = None
        if not isinstance(name, (str)):
            raise TypeError('Имена друзей должны быть типа str')
        self.name = name
        if not isinstance(country, (str)):
            raise TypeError('Параметра страна должен быть типа str')
        self.country = country
    def init_age(self, age:int):
        if not isinstance(age, (int)):
            raise TypeError('Возраст друзей должен быть типа int')
        if age < 0:
            raise ValueError('Возраст друзей должен быть положительным')
        self.age = age
    def init_number(self,number:int):
        if not isinstance(number, (int)):
            raise TypeError
        if number < 0:
            raise ValueError
        self.number = number
    def grow_age(self, current_year, year_of_birth):
        self.age = current_year - year_of_birth
        return age
    def increase_number(self, new_number:int):
        """
        Функция, которая увеличивает количество друзей
        :param new_number: Число новых друзей
        :return: Количество друзей
        :raise TypeError: Если параметр new_number не принадлежит int
        """
        if not isinstance(new_number, (int)):
            raise TypeError
        ...

class Warehouse:
    def __init__(self, cargo_turnover: Union[int, float], time_of_keeping:int, type_of_cargo:str, warehouse_area:int):
        """
        Создание и подготовка к работе объекта "Склад"
        :param cargo_turnover: Грузооборот склада
        :param time_of_keeping: Срок хранения
        :param type_of_cargo: Тип груза
        :param warehouse_area: Площадь склада

        Примеры:
        >>> warehouse = Warehouse(800, 10, "pallets", 12000)
        """
        if not isinstance(cargo_turnover,(int,float)):
            raise TypeError
        if cargo_turnover <= 0:
            raise ValueError
        self.cargo_turnover = cargo_turnover

        if not isinstance(time_of_keeping, (int)):
            raise TypeError
        if time_of_keeping <= 0:
            raise ValueError
        self.time_of_keeping = time_of_keeping

        if not isinstance(type_of_cargo,(str)):
            raise TypeError

        if not isinstance(warehouse_area, (int)):
            raise TypeError

    def add_cargo_turnover(self, tonne:float)->int:
        """
        Добавление грузооборота
        :param tonne: Масса добавляемого грузооборота
        """
        ...
    def change_warehouse_area(self, length, width, height):
        """

        :param length: Длина склада
        :param width: Ширина склада
        :param height: Высота склада
        :return: Новая площадь склада
        """

class Pancake:
    def __init__(self, eggs:int, milk:int, sugar:int, flour:int):
        """
        Создание и подготовка к работе объекта "Панкейки"
        :param eggs: Количество яиц
        :param milk: Количество молока
        :param sugar: Количество сахара
        :param flour: Количество мука
        Примеры:
        >>> pancake = Pancake(2,500, 200, 250)
        """
        if not isinstance(eggs,(int)):
            raise TypeError
        if eggs < 0:
            raise ValueError
        self.eggs = eggs

        if not isinstance(milk, (int)):
            raise TypeError
        if milk < 0:
            raise ValueError
        self.milk = milk

        if not isinstance(sugar,(int)):
            raise TypeError
        if sugar < 0:
            raise ValueError
        self.sugar = sugar

        if not isinstance(flour, (int)):
            raise TypeError
        if flour < 0:
            raise ValueError
        self.flour = flour

    def add_cacao_to_pancake(self, cacao:int):
        """
        Добавление какое в панкейки
        :param cacao: Количество добавляемого какое
        :return: Новый рецепт панкейков
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass