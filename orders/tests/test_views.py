from django.test import Client
from django.urls import resolve

from orders.views import index, sign_up


class TestIndex:
    """all tests relating to the index route"""

    def test_root_resolves_to_index_view(self):
        found = resolve("/")
        assert found.func == index
    
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

    def test_sign_up_resolves_to_sign_up_view(self):
        found = resolve("/sign_up")
        assert found.func == sign_up

    def test_get_sign_up_status_code(self):
        """register route redirects to index"""

        c = Client()
        response = c.get("/sign_up")
        assert response.status_code == 200

    def test_sign_in_redirects(self):
        """sign in route redirects to index"""

        c = Client()
        response = c.get("/sign_in")
        assert response.status_code == 302
