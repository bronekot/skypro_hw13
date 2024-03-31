import pytest
from classes.category import Category
from classes.product import Product

import main

def test_category_initialization():
    category = Category("Электроника", "Электронные устройства и гаджеты")
    assert category.name == "Электроника"
    assert category.description == "Электронные устройства и гаджеты"
    assert len(category.products) == 0
    assert Category.total_categories == 1
    assert Category.total_unique_products == 0


def test_product_initialization():
    product = Product("Ноутбук", "Мощный ноутбук для работы и игр", 1000, 10)
    assert product.name == "Ноутбук"
    assert product.description == "Мощный ноутбук для работы и игр"
    assert product.price == 1000
    assert product.quantity == 10


def test_product_count():
    Category.total_categories = 0
    Category.__unique_products = set()
    category = Category("Электроника", "Электронные устройства и гаджеты")
    laptop = Product("Ноутбук", "Мощный ноутбук для работы и игр", 1000, 10)
    tablet = Product("Планшет", "Портативный планшет для мультимедиа", 500, 5)
    category.add_product(laptop)
    category.add_product(tablet)
    assert len(category.products) == 2
    assert Category.total_unique_products == 2


def test_category_count():
    Category.total_categories = 0
    category1 = Category("Электроника", "Электронные устройства и гаджеты")
    category2 = Category("Книги", "Книги для чтения")
    assert Category.total_categories == 2
