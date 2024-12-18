# Ecommerce1

A Flask-based ecommerce application with modular architecture and SQLAlchemy integration.

## Features

- Product management
- Customer management 
- Order processing
- RESTful API endpoints
- SQLAlchemy database integration

## Project Structure


Copy

Apply

README.md
ecommerce1/ ├── app/ │ ├── init.py │ ├── services/ │ │ ├── product_service.py │ │ ├── customer_service.py │ │ └── order_service.py │ └── models/ ├── config.py └── README.md


## Setup

1. Create a virtual environment:
```bash
python -m venv venv

Copy

Apply

Activate the virtual environment:
source venv/bin/activate

Copy

Execute

Install dependencies:
pip install -r requirements.txt

Copy

Execute

Run the application:
flask run

Copy

Execute

API Endpoints
Products
GET /products - List all products
POST /products - Create a new product
Customers
GET /customers - List all customers
POST /customers - Create a new customer
Orders
GET /orders - List all orders
POST /orders - Create a new order
Development
The application uses a modular architecture with:

Blueprint-based routing
Service layer for business logic
SQLAlchemy for database operations
Automatic database table creation on startup
Configuration
The application supports different configuration environments through the config_class parameter in create_app().

Contributing
Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Create a Pull Request