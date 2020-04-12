from django.urls import resolve
import pytest

from orders.views import index, sign_up


class TestIndex:
    """all tests relating to the index route"""

    def test_root_resolves_to_index_view(self):
        found = resolve("/")
        assert found.func == index
    
    @pytest.mark.django_db
    def test_index_status_code(self, client):
        """index route returns status code 200"""

        response = client.get("/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_index_template_used(self, client):
        """index route uses index.html template"""

        response = client.get("/")
        assert 'orders/index.html' in (t.name for t in response.templates)


class TestSignUp:
    def test_sign_up_resolves_to_sign_up_view(self):
        found = resolve("/sign_up")
        assert found.func == sign_up

    def test_get_sign_up_status_code(self, client):
        """register route redirects to index"""

        response = client.get("/sign_up")
        assert response.status_code == 200

    def test_log_out_redirects(self, client):
        """log out route redirects to index"""

        response = client.get("/log_out")
        assert response.status_code == 302
