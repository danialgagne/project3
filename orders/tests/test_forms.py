from orders.forms import UserCreationForm
import pytest


@pytest.mark.django_db
def test_sign_up_form():
    form_data = {
        'username': 'pytesttester',
        'password1': 'JustAPassword1',
        'password2': 'JustAPassword1',
        'email': 'tester@ordersapp.com',
        'first_name': 'Danial',
        'last_name': 'Gagne'
    }
    form = UserCreationForm(form_data)
    assert form.is_valid()
