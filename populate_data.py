import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings')
django.setup()

from categories.models import Category
from products.models import Product
from decimal import Decimal

# Create Categories
categories_data = [
    {'name': 'Electronics', 'slug': 'electronics', 'description': 'Electronic devices and gadgets'},
    {'name': 'Clothing', 'slug': 'clothing', 'description': 'Fashion and apparel'},
    {'name': 'Books', 'slug': 'books', 'description': 'Books and literature'},
    {'name': 'Home & Garden', 'slug': 'home-garden', 'description': 'Home improvement and garden'},
    {'name': 'Sports', 'slug': 'sports', 'description': 'Sports equipment and gear'},
]

for cat_data in categories_data:
    Category.objects.get_or_create(**cat_data)

print("Categories created successfully!")

# Create Products
electronics = Category.objects.get(slug='electronics')
clothing = Category.objects.get(slug='clothing')

products_data = [
    {'name': 'Laptop Pro 15"', 'slug': 'laptop-pro-15', 'category': electronics,
     'price': Decimal('1299.99'), 'stock_quantity': 50, 'description': 'High-performance laptop', 'featured': True},
    {'name': 'Wireless Mouse', 'slug': 'wireless-mouse', 'category': electronics,
     'price': Decimal('29.99'), 'stock_quantity': 200, 'description': 'Ergonomic wireless mouse'},
    {'name': 'Cotton T-Shirt', 'slug': 'cotton-tshirt', 'category': clothing,
     'price': Decimal('19.99'), 'stock_quantity': 100, 'description': '100% cotton t-shirt'},
]

for prod_data in products_data:
    Product.objects.get_or_create(**prod_data)

print("Products created successfully!")