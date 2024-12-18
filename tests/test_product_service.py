import unittest
from app.services.product_service import ProductService
from app.models import Product
from app.db import db
from unittest.mock import MagicMock


class TestProductService(unittest.TestCase):

    def setUp(self):
        """Set up the test database before each test"""
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test_user:test_password@localhost:5432/test_db"
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up the database after each test"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_product(self):
        """Test adding a product"""
        data = {
            "name": "Smartphone",
            "price": 599.99,
            "stock": 50
        }
        product_service = ProductService()
        product = product_service.add_product(data)

        self.assertEqual(product.name, "Smartphone")
        self.assertEqual(product.price, 599.99)
        self.assertEqual(product.stock, 50)

    def test_get_product_by_id(self):
        """Test fetching a product by ID"""
        product_service = ProductService()
        product_service.add_product({
            "name": "Smartphone",
            "price": 599.99,
            "stock": 50
        })

        product = product_service.get_product_by_id(1)
        self.assertEqual(product.name, "Smartphone")
        self.assertEqual(product.price, 599.99)

    def test_update_product(self):
        """Test updating a product"""
        product_service = ProductService()
        product_service.add_product({
            "name": "Smartphone",
            "price": 599.99,
            "stock": 50
        })

        data = {
            "price": 549.99,
            "stock": 45
        }
        updated_product = product_service.update_product(1, data)
        self.assertEqual(updated_product.price, 549.99)
        self.assertEqual(updated_product.stock, 45)

    def test_delete_product(self):
        """Test deleting a product"""
        product_service = ProductService()
        product_service.add_product({
            "name": "Smartphone",
            "price": 599.99,
            "stock": 50
        })

        product_service.delete_product(1)
        product = product_service.get_product_by_id(1)
        self.assertIsNone(product)
