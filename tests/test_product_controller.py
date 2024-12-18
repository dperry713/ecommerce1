import unittest
from app import create_app
from app.db import db
from flask import json


class TestProductController(unittest.TestCase):

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

    def test_create_product(self):
        """Test POST /products"""
        data = {
            "name": "Smartphone",
            "price": 599.99,
            "stock": 50
        }
        response = self.client.post('/products', json=data)
        self.assertEqual(response.status_code, 201)
        json_data = json.loads(response.data)
        self.assertEqual(json_data["name"], "Smartphone")
        self.assertEqual(json_data["price"], 599.99)

    def test_get_product(self):
        """Test GET /products/<id>"""
        data = {
            "name": "Smartphone",
            "price": 599.99,
            "stock": 50
        }
        self.client.post('/products', json=data)
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
        self.assertEqual(json_data["name"], "Smartphone")

    def test_update_product(self):
        """Test PUT /products/<id>"""
        data = {
            "name": "Smartphone",
            "price": 599.99,
            "stock": 50
        }
        self.client.post('/products', json=data)
        updated_data = {
            "price": 549.99,
            "stock": 45
        }
        response = self.client.put('/products/1', json=updated_data)
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
        self.assertEqual(json_data["price"], 549.99)
        self.assertEqual(json_data["stock"], 45)

    def test_delete_product(self):
        """Test DELETE /products/<id>"""
        data = {
            "name": "Smartphone",
            "price": 599.99,
            "stock": 50
        }
        self.client.post('/products', json=data)
        response = self.client.delete('/products/1')
        self.assertEqual(response.status_code, 204)
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 404)
