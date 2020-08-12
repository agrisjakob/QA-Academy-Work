from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app1 import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_cat(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                p.return_value.text= "meow"
                g.return_value.text = "cat"
                response = self.client.get(url_for('generate'))
                self.assertIn(b'meow', response.data)
    
    def test_dog(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                p.return_value.text= "woof"
                g.return_value.text= "dog"
                response = self.client.get(url_for('generate'))
                self.assertIn(b'woof', response.data)

    def test_home_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_port(self):
        response = self.client.get('localhost:5000')
        self.assertEqual(response.status_code, 200)
