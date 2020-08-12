from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from app2 import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_animal_api(self):
            response = self.client.get('/animal')
            answers = ["dog", "cat", "chicken"]
            assert response.data.decode('utf-8') in answers

    def test_noise_api_dog(self):
                response = self.client.post('/noise', data="dog")
                self.assertIn(b'woof', response.data)
    def test_noise_api_cat(self):
                response = self.client.post('/noise', data="cat")
                self.assertIn(b'meow', response.data)
    def test_noise_api_chicken(self):
                response = self.client.post('/noise', data="chicken")
                self.assertIn(b'bwuk', response.data)
    def test_noise_api_none(self):
                response = self.client.post('/noise', data="horse")
                self.assertIn(b'no animal selected', response.data)
