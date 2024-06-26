
from abc import ABC, abstractmethod

from classes.mixins import mixinRepr


class Products(ABC):
    @abstractmethod
    def price(self):
        pass


class Product(Products, mixinRepr):
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            print("товар с нулевым количеством не может быть добавлен")
            raise ValueError
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @staticmethod
    def new(name, description, price, quantity):
        return Product(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Некорректная цена (должна быть больше 0)")
            return
        if new_price < self.__price:
            answer = input("Новая цена меньше старой, если вы хотите изменить введите Y")
            if answer.lower() != "y":
                print("Цена НЕ изменена")
                return
        self.__price = new_price
        print("Цена изменена")

    def __add__(self, other):
        if isinstance(other, self.__class__):
            raise ValueError("Нельзя сложить разные типы продуктов")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return (f"Товар: {self.name} ({self.description}) - "
                f"Цена: {self.__price}, Количество: {self.quantity}")


# производительность,
# модель,
# объем встроенной памяти,
# цвет.
class Smartphone(Product):

    def __init__(self, name, description, price, perfomance, model, memory, color,
                 quantity):
        super().__init__(name, description, price, quantity)
        self.perfomance = perfomance
        self.model = model
        self.memory = memory
        self.color = color


# страна-производитель,
# срок прорастания,
# цвет.
class LawnGrass(Product):

    def __init__(self, name, description, price, country, germination_period, color,
                 quantity):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
