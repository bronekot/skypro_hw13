from typing import List
from .product import Product


class Category:
    total_categories = 0
    __unique_products = set()

    def __init__(self, name: str, description: str, products: List[Product] = []):
        self.name = name
        self.description = description
        self.__products: List[Product] = products
        Category.total_categories += 1

    def add_product(self, product: Product):
        for p in self.__products:
            if p.name == product.name:
                if p.price < product.price:
                    p.price = product.price
                p.quantity += product.quantity
                return
        self.__products.append(product)
        if product.name not in Category.__unique_products:
            Category.__unique_products.add(product.name)

    @property
    def products(self):
        for product in self.__products:
            print(product)

    def remove_product(self, product: Product):
        self.__products.remove(product)
        if product.quantity == 0:
            Category.__unique_products.remove(product.name)

    @classmethod
    @property
    def total_unique_products(cls):
        return len(cls.__unique_products)

    def __str__(self):
        return f"Категория: {self.name} ({self.description})"
