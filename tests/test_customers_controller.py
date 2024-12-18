import unittest
from app import create_app
from app.db import db
from flask import json


class TestCustomerController(unittest.TestCase):

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

    def test_create_customer(self):
        """Test POST /customers"""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890"
        }
        response = self.client.post('/customers', json=data)
        self.assertEqual(response.status_code, 201)
        json_data = json.loads(response.data)
        self.assertEqual(json_data["first_name"], "John")
        self.assertEqual(json_data["last_name"], "Doe")
        self.assertEqual(json_data["email"], "john.doe@example.com")
        self.assertEqual(json_data["phone"], "1234567890")

    def test_get_customer(self):
        """Test GET /customers/<id>"""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890"
        }
        self.client.post('/customers', json=data)
        response = self.client.get('/customers/1')
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
        self.assertEqual(json_data["first_name"], "John")
        self.assertEqual(json_data["last_name"], "Doe")
        self.assertEqual(json_data["email"], "john.doe@example.com")

    def test_update_customer(self):
        """Test PUT /customers/<id>"""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890"
        }
        self.client.post('/customers', json=data)
        updated_data = {
            "email": "johnny.doe@example.com",
            "phone": "9876543210"
        }
        response = self.client.put('/customers/1', json=updated_data)
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
        self.assertEqual(json_data["email"], "johnny.doe@example.com")
        self.assertEqual(json_data["phone"], "9876543210")

    def test_delete_customer(self):
        """Test DELETE /customers/<id>"""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890"
        }
        self.client.post('/customers', json=data)
        response = self.client.delete('/customers/1')
        self.assertEqual(response.status_code, 204)
        response = self.client.get('/customers/1')
        self.assertEqual(response.status_code, 404)
