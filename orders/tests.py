from django.test import TestCase
import pytest

from .models import Category


@pytest.mark.django_db
class TestCategory:

    def test_create_category(self):
        """Test adding records to the Category Model"""
        c1 = Category.objects.create(name="Pizza")
        c2 = Category.objects.create(name="Salads")
        categories = Category.objects.all()
        assert categories.count() == 2

