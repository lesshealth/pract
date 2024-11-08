import unittest
from app import app, db
from models import User

class RegistrationAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_successful_registration(self):
        response = self.app.post('/api/register', json={
            "name": "Андрей",
            "email": "andrey1234@gmail.com",
            "password": "safeonefrngl"
        })
        self.assertEqual(response.status_code, 200)

    def test_missing_email(self):
        response = self.app.post('/api/register', json={
            "name": "Андрей",
            "password": "safeonefrngl"
        })
        self.assertEqual(response.status_code, 400)

    def test_short_password(self):
        response = self.app.post('/api/register', json={
            "name": "Андрей",
            "email": "andrey1234@gmail.com",
            "password": "short"
        })
        self.assertEqual(response.status_code, 400)

        # curl -X POST http://127.0.0.1:5000/api/register -H "Content-Type: application/json" -d "{\"name\":\"Андрей\", \"email\":\"andrey1234@gmail.com\", \"password\":\"safeonefrngl\"}"


if __name__ == '__main__':
    unittest.main()