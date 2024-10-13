# test_app.py : Tests unitaires pour l'application Flask

import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), 'Hello, OpenShift!')

if __name__ == '__main__':
    unittest.main()
