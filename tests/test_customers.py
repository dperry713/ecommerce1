import unittest
from app import create_app
from app.db import db
from flask import json
from app.services.customer_service import CustomerService


class TestCustomerService(unittest.TestCase):

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

    def test_add_customer(self):
        """Test adding a customer"""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890"
        }
        customer_service = CustomerService()
        customer = customer_service.add_customer(data)

        self.assertEqual(customer.first_name, "John")
        self.assertEqual(customer.last_name, "Doe")
        self.assertEqual(customer.email, "john.doe@example.com")
        self.assertEqual(customer.phone, "1234567890")

    def test_get_customer_by_id(self):
        """Test fetching a customer by ID"""
        customer_service = CustomerService()
        customer_service.add_customer({
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890"
        })

        customer = customer_service.get_customer_by_id(1)
        self.assertEqual(customer.first_name, "John")
        self.assertEqual(customer.last_name, "Doe")
        self.assertEqual(customer.email, "john.doe@example.com")

    def test_update_customer(self):
        """Test updating a customer"""
        customer_service = CustomerService()
        customer_service.add_customer({
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890"
        })

        data = {
            "email": "johnny.doe@example.com",
            "phone": "9876543210"
        }
        updated_customer = customer_service.update_customer(1, data)
        self.assertEqual(updated_customer.email, "johnny.doe@example.com")
        self.assertEqual(updated_customer.phone, "9876543210")

    def test_delete_customer(self):
        """Test deleting a customer"""
        customer_service = CustomerService()
        customer_service.add_customer({
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890"
        })

        customer_service.delete_customer(1)
        customer = customer_service.get_customer_by_id(1)
        self.assertIsNone(customer)
