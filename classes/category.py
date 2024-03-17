from typing import List
from .product import Product


class Category:
    total_categories = 0
    unique_products = set()

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products: List[Product] = []
        Category.total_categories += 1

    def add_product(self, product: Product):
        self.products.append(product)
        if product not in Category.unique_products:
            Category.unique_products.add(product)

    def remove_product(self, product: Product):
        self.products.remove(product)
        if product.quantity == 0:
            Category.unique_products.remove(product)

    @classmethod
    @property
    def total_unique_products(cls):
        return len(cls.unique_products)

    def __str__(self):
        return f"Категория: {self.name} ({self.description})"
