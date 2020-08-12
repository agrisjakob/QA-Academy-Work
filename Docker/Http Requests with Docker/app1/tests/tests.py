from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app1 import app1

class TestBase(TestCase):
    def create_app(self):
        return app1


class TestResponse(TestBase):

    def test_cat:
        with patch('requests.get') as g:
            g.return_value.text = "cat"
            response = self.client.get(url_for('generate'))
            self.assertIn(b'meow', response.data)
