from typing import List
from classes.product import Product


class Category:
    total_categories = 0
    __unique_products = 0

    def __init__(self, name: str, description: str, products: List[Product] = []):
        self.name = name
        self.description = description
        self.__products: List[Product] = products
        Category.total_categories += 1
        for p in products:
            self.add_product(p)

    def add_product(self, product: Product):
        for p in self.__products:
            if p.name == product.name:
                if p.price < product.price:
                    p.price = product.price
                p.quantity += product.quantity
                return
        self.__products.append(product)
        Category.__unique_products += 1

    @property
    def products(self):
        for product in self.__products:
            print(product)

    @classmethod
    def total_unique_products(cls):
        return cls.__unique_products

    def __len__(self):
        len_products = 0
        for p in self.__products:
            len_products += p.quantity
        return len_products

    def __str__(self):
        return f"Категория: {self.name} ({self.description})"
