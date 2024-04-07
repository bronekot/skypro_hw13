class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        if new_price <= 0:
            print("Некорректная цена (должна быть больше 0)")
            return
        if new_price < self.price:
            answer = input("Новая цена меньше старой, если вы хотите изменить введите Y")
            if answer.lower() != "y":
                print("Цена НЕ изменена")
                return
        self.price = new_price
        print("Цена изменена")

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"Товар: {self.name} ({self.description}) - Цена: {self.price}, Количество: {self.quantity}"