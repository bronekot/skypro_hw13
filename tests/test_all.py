import pytest


from classes.category import Category
from classes.product import Product


def test_category_initialization():
    category = Category("Электроника", "Электронные устройства и гаджеты")
    assert category.name == "Электроника"
    assert category.description == "Электронные устройства и гаджеты"
    assert len(category._Category__products) == 0
    assert Category.total_categories == 1
    assert Category.total_unique_products() == 0


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
    laptop = Product.new("Ноутбук", "Мощный ноутбук для работы и игр", 1000, 10)
    tablet = Product.new("Планшет", "Портативный планшет для мультимедиа", 500, 5)
    category.add_product(laptop)
    category.add_product(tablet)
    assert len(category._Category__products) == 2
    assert Category.total_unique_products() == 2


def test_category_count():
    Category.total_categories = 0
    category1 = Category("Электроника", "Электронные устройства и гаджеты")
    category2 = Category("Книги", "Книги для чтения")
    assert Category.total_categories == 2


def test_negative_price():
    product = Product.new("Test Product", "Description", 100, 1)  # Здесь подставьте ваш класс и начальную цену
    product.price = -50
    assert product.price == 100  # Проверка, что цена осталась прежней


def test_lower_price_confirmation(monkeypatch: pytest.MonkeyPatch):
    product = Product.new("Test Product", "Description", 100, 1)  # Здесь подставьте ваш класс и начальную цену
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    product.price = 50
    assert product.price == 50  # Проверка, что цена изменилась при подтверждении


def test_lower_price_no_confirmation(monkeypatch: pytest.MonkeyPatch):
    product = Product.new("Test Product", "Description", 100, 1)  # Здесь подставьте ваш класс и начальную цену
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    product.price = 50
    assert product.price == 100  # Проверка, что цена не изменилась без подтверждения


def test_add_product():
    category = Category("Test Category", "Test Description")
    product1 = Product.new("Product1", "Description", 10, 1)
    product2 = Product.new("Product2", "Description", 20, 1)

    # Adding a new product
    category.add_product(product1)
    assert product1 in category._Category__products
    assert product1.name in Category._Category__unique_products

    # Adding a product with the same name but higher price
    category.add_product(Product("Product1", "New Description", 15, 2))
    assert product1.price == 15
    assert product1.quantity == 3

    # Adding a product with the same name but lower price
    category.add_product(Product("Product1", "Lower Price", 5, 1))
    assert product1.price == 15  # Price should remain unchanged
    assert product1.quantity == 4

    # Adding a completely new product
    category.add_product(product2)
    assert product2 in category._Category__products
    assert product2.name in Category._Category__unique_products
