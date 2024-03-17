class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Товар: {self.name} ({self.description}) - Цена: {self.price}, Количество: {self.quantity}"