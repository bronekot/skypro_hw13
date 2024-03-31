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
            print("Некорректная цена")
            return
        if new_price < self.price:
            answer = input("Новая цена меньше старой, если вы хотите изменить введите Y")
            if answer.lower() != "y":
                return
        self.price = new_price

    def __str__(self):
        return f"Товар: {self.name} ({self.description}) - Цена: {self.price}, Количество: {self.quantity}"