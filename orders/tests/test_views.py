from django.test import Client
import pytest


class TestIndex:
    """all tests relating to the index route"""
    def test_status_code(self):
        """root route returns status code 200"""
        c = Client()
        response = c.get("/")
        assert response.status_code == 200