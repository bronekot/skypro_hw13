class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    def __str__(self):
        return f"Товар: {self.name} ({self.description}) - Цена: {self.__price}, Количество: {self.quantity}"