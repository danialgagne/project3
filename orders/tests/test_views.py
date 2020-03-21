from django.test import Client
import pytest


class TestIndex:
    """all tests relating to the index route"""

    def test_index_status_code(self):
        """index route returns status code 200"""

        c = Client()
        response = c.get("/")
        assert response.status_code == 200

    def test_index_template_used(self):
        """index route uses index.html template"""

        c = Client()
        response = c.get("/")
        assert 'orders/index.html' in (t.name for t in response.templates)

    def test_register_redirects(self):
        """register route redirects to index"""

        c = Client()
        response = c.get("/register")
        assert response.status_code == 302