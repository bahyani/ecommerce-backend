# 🛒 E-Commerce Backend API - Project Nexus

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.14-red.svg)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A production-ready, scalable RESTful API backend for e-commerce applications built with Django REST Framework and PostgreSQL.

## 📖 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Database Schema](#-database-schema)
- [API Endpoints](#-api-endpoints)
- [Authentication](#-authentication)
- [Query Parameters](#-query-parameters)
- [Performance Optimization](#-performance-optimization)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Core Functionality
- ✅ **JWT Authentication** - Secure token-based authentication with refresh tokens
- ✅ **User Management** - Complete user registration, login, and profile management
- ✅ **Product Catalog** - Full CRUD operations for products with image support
- ✅ **Category Management** - Hierarchical product categorization
- ✅ **Advanced Filtering** - Filter by category, price range, availability, and featured status
- ✅ **Search Functionality** - Full-text search across product names and descriptions
- ✅ **Sorting & Ordering** - Sort by price, name, date, and stock quantity
- ✅ **Pagination** - Efficient data retrieval with customizable page sizes

### Technical Features
- ⚡ **Database Optimization** - Composite indexes for high-performance queries
- 📚 **API Documentation** - Interactive Swagger/OpenAPI documentation
- 🔒 **Security** - Password hashing, CORS configuration, SQL injection protection
- 🎨 **RESTful Design** - Clean, consistent API following REST principles
- 📊 **Admin Dashboard** - Django admin interface for content management

---

## 🛠️ Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Django** | Web Framework | 4.2.7 |
| **Django REST Framework** | API Development | 3.14.0 |
| **PostgreSQL** | Database | 14+ |
| **JWT** | Authentication | 5.3.0 |
| **Swagger/OpenAPI** | API Documentation | 1.21.7 |
| **Python** | Programming Language | 3.10+ |

**Additional Libraries:**
- `django-filter` - Advanced filtering
- `django-cors-headers` - CORS handling
- `Pillow` - Image processing
- `python-decouple` - Environment management

---

## 🏗️ Architecture

### Database Schema (ERD)

```
┌─────────────┐          ┌──────────────┐
│    USER     │          │   CATEGORY   │
├─────────────┤          ├──────────────┤
│ PK id       │          │ PK id        │
│ username    │          │ name         │
│ email       │          │ slug         │
│ password    │          │ description  │
│ ...         │          │ is_active    │
└─────────────┘          └──────────────┘
                                │
                                │ 1
                                │
                                │
                                │ N
                         ┌──────────────┐
                         │   PRODUCT    │
                         ├──────────────┤
                         │ PK id        │
                         │ FK category  │
                         │ name         │
                         │ slug         │
                         │ price        │
                         │ stock        │
                         │ image        │
                         │ featured     │
                         │ is_active    │
                         └──────────────┘
```

### Project Structure

```
ecommerce-backend/
│
├── ecommerce_backend/          # Project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL routing
│   └── wsgi.py                 # WSGI configuration
│
├── users/                      # User authentication app
│   ├── models.py               # Custom User model
│   ├── serializers.py          # User serializers
│   ├── views.py                # Authentication views
│   └── urls.py                 # User endpoints
│
├── products/                   # Product management app
│   ├── models.py               # Product model
│   ├── serializers.py          # Product serializers
│   ├── views.py                # Product CRUD views
│   ├── filters.py              # Custom filters
│   └── urls.py                 # Product endpoints
│
├── categories/                 # Category management app
│   ├── models.py               # Category model
│   ├── serializers.py          # Category serializers
│   ├── views.py                # Category views
│   └── urls.py                 # Category endpoints
│
├── media/                      # User-uploaded files
├── scripts/                    # Utility scripts
├── requirements.txt            # Python dependencies
└── manage.py                   # Django management script
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- PostgreSQL 14 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-backend.git
cd ecommerce-backend
```

#### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Set Up PostgreSQL Database

```bash
# Access PostgreSQL
psql -U postgres

# Create database and user
CREATE DATABASE ecommerce_db;
CREATE USER ecommerce_user WITH PASSWORD 'your_secure_password';
ALTER ROLE ecommerce_user SET client_encoding TO 'utf8';
ALTER ROLE ecommerce_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ecommerce_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ecommerce_db TO ecommerce_user;
\q
```

#### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key-here-generate-strong-one
DEBUG=True
DB_NAME=ecommerce_db
DB_USER=ecommerce_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432
```

**Generate a secure SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. Create Superuser

```bash
python manage.py createsuperuser
```

#### 8. Load Sample Data (Optional)

```bash
python scripts/populate_data.py
```

#### 9. Run Development Server

```bash
python manage.py runserver
```

The API will be available at: **http://localhost:8000/**

---

## 📚 API Documentation

### Interactive Documentation

- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/
- **Admin Panel**: http://localhost:8000/admin/

### Quick API Overview

| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/users/register/` | POST | Register new user | No |
| `/api/users/login/` | POST | Login and get tokens | No |
| `/api/users/profile/` | GET | Get user profile | Yes |
| `/api/products/` | GET | List all products | No |
| `/api/products/` | POST | Create product | Yes (Admin) |
| `/api/products/{slug}/` | GET | Get product detail | No |
| `/api/products/{slug}/` | PUT | Update product | Yes (Admin) |
| `/api/products/{slug}/` | DELETE | Delete product | Yes (Admin) |
| `/api/categories/` | GET | List categories | No |

---

## 🗄️ Database Schema

### User Model

```python
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "+1234567890",
  "address": "123 Main St",
  "created_at": "2024-01-01T00:00:00Z"
}
```

### Category Model

```python
{
  "id": 1,
  "name": "Electronics",
  "slug": "electronics",
  "description": "Electronic devices and gadgets",
  "is_active": true,
  "product_count": 25,
  "created_at": "2024-01-01T00:00:00Z"
}
```

### Product Model

```python
{
  "id": 1,
  "name": "Laptop Pro 15",
  "slug": "laptop-pro-15",
  "description": "High-performance laptop",
  "category_details": {
    "id": 1,
    "name": "Electronics",
    "slug": "electronics"
  },
  "price": "1299.99",
  "stock_quantity": 50,
  "image": "/media/products/laptop.jpg",
  "is_active": true,
  "featured": true,
  "in_stock": true,
  "created_at": "2024-01-01T00:00:00Z"
}
```

---

## 🔌 API Endpoints

### Authentication Endpoints

#### Register User
```http
POST /api/users/register/
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "password2": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response:**
```json
{
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  "message": "User registered successfully"
}
```

#### Login
```http
POST /api/users/login/
Content-Type: application/json

{
  "username": "johndoe",
  "password": "SecurePass123!"
}
```

**Response:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Product Endpoints

#### List Products (with filtering)
```http
GET /api/products/?category=electronics&min_price=100&max_price=500&ordering=-price&page=1
```

#### Create Product (Admin only)
```http
POST /api/products/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "Wireless Mouse",
  "slug": "wireless-mouse",
  "description": "Ergonomic wireless mouse",
  "category": 1,
  "price": "29.99",
  "stock_quantity": 100,
  "featured": false
}
```

#### Get Product Detail
```http
GET /api/products/wireless-mouse/
```

#### Update Product (Admin only)
```http
PUT /api/products/wireless-mouse/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "Wireless Mouse Pro",
  "price": "39.99",
  "stock_quantity": 150
}
```

#### Delete Product (Admin only)
```http
DELETE /api/products/wireless-mouse/
Authorization: Bearer {access_token}
```

---

## 🔐 Authentication

This API uses **JWT (JSON Web Tokens)** for authentication.

### How to Authenticate

1. **Register** or **Login** to get tokens
2. Include the access token in subsequent requests:

```http
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

### Token Refresh

When your access token expires (60 minutes), use the refresh token:

```http
POST /api/users/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

---

## 🔍 Query Parameters

### Filtering Products

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `category` | string | Filter by category slug | `?category=electronics` |
| `min_price` | decimal | Minimum price | `?min_price=100` |
| `max_price` | decimal | Maximum price | `?max_price=500` |
| `in_stock` | boolean | Only in-stock items | `?in_stock=true` |
| `featured` | boolean | Only featured products | `?featured=true` |
| `is_active` | boolean | Only active products | `?is_active=true` |

### Searching

```http
GET /api/products/?search=laptop
```

Searches across: `name`, `description`

### Sorting

| Parameter | Description |
|-----------|-------------|
| `?ordering=price` | Sort by price (ascending) |
| `?ordering=-price` | Sort by price (descending) |
| `?ordering=name` | Sort by name (A-Z) |
| `?ordering=-created_at` | Newest first |
| `?ordering=stock_quantity` | Sort by stock |

### Pagination

```http
GET /api/products/?page=2&page_size=10
```

Default page size: **20 items**

### Combined Example

```http
GET /api/products/?category=electronics&min_price=100&max_price=1000&in_stock=true&ordering=-price&page=1&page_size=15
```

---

## ⚡ Performance Optimization

### Database Indexes

Our database uses strategic indexing for optimal performance:

#### Single-Column Indexes
- `users.email` (UNIQUE)
- `users.username` (UNIQUE)
- `categories.slug` (UNIQUE)
- `products.slug` (UNIQUE)
- `products.category_id` (Foreign Key)
- `products.price`
- `products.is_active`
- `products.featured`
- `products.created_at` (Descending)

#### Composite Indexes
- `(category_id, created_at)` - For "newest in category" queries
- `(is_active, price)` - For active product price filtering

### Query Optimization

```python
# Bad: N+1 query problem
products = Product.objects.all()
for product in products:
    print(product.category.name)  # Extra query per product!

# Good: Uses select_related
products = Product.objects.select_related('category').all()
for product in products:
    print(product.category.name)  # No extra queries!
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test products

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### API Testing with cURL

```bash
# Register user
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"Test123!","password2":"Test123!"}'

# Login
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"Test123!"}'

# Get products
curl http://localhost:8000/api/products/
```

---

## 🌐 Deployment

### Environment Setup

For production, update your `.env`:

```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=your-production-secret-key
```

### Deployment Platforms

#### Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create app
heroku create your-ecommerce-api

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

#### Railway

1. Connect your GitHub repository
2. Add PostgreSQL plugin
3. Set environment variables
4. Deploy automatically on push

#### DigitalOcean App Platform

1. Create new app from GitHub
2. Add PostgreSQL database
3. Configure environment variables
4. Deploy

---

## 📝 Git Workflow

### Commit Message Convention

Follow the conventional commits specification:

```bash
feat: add product filtering by price range
fix: resolve category deletion cascade issue
perf: optimize database queries with indexing
docs: update API documentation in README
chore: update dependencies to latest versions
test: add unit tests for product serializers
```

### Example Workflow

```bash
# Create feature branch
git checkout -b feat/add-reviews

# Make changes and commit
git add .
git commit -m "feat: add product review functionality"

# Push to remote
git push origin feat/add-reviews

# Create pull request on GitHub
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Write meaningful commit messages
- Add docstrings to functions and classes
- Write unit tests for new features

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**[Your Name]**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- Django REST Framework documentation
- PostgreSQL documentation
- Project Nexus mentors and community

---

## 📞 Support

For issues, questions, or contributions, please:
- Open an issue on GitHub
- Email: support@example.com
- Join our Discord community

---

## 🗺️ Roadmap

### Phase 1 (Current) ✅
- [x] User authentication
- [x] Product CRUD
- [x] Category management
- [x] Filtering & search
- [x] API documentation

### Phase 2 (Upcoming)
- [ ] Shopping cart functionality
- [ ] Order management
- [ ] Payment integration
- [ ] Email notifications
- [ ] Advanced analytics

### Phase 3 (Future)
- [ ] Product reviews & ratings
- [ ] Wishlist feature
- [ ] Inventory management
- [ ] Multi-vendor support
- [ ] Advanced reporting

---

**⭐ If you find this project helpful, please give it a star!**

Made with ❤️ for Project Nexus