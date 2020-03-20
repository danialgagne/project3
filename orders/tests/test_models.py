import pytest

from orders.models import Category, Item, Topping


pytestmark = pytest.mark.django_db

class TestCategory:

    def test_create_category(self):
        """Test adding records to the Category model"""
        c1 = Category.objects.create(name="Pizza")
        c2 = Category.objects.create(name="Salads")
        categories = Category.objects.all()
        assert categories.count() == 2



class TestItem:

    def test_create_item(self):
        """Test adding records to the Item model"""
        category = Category.objects.create(name="Pizza")

        item = Item.objects.create(
            name="1 Topping",
            category=category,
            large_price=14.50,
            toppings_allowed=True
        )
        items = Item.objects.all()
        assert items.count() == 1



class TestTopping:

    def test_create_topping(self):
        """Test adding records to the Topping model"""
        category = Category.objects.create(name="Pizza")

        t1 = Topping.objects.create(name="Pepperoni", category=category)
        t2 = Topping.objects.create(name="Sausage", category=category)
        t3 = Topping.objects.create(name="Mushrooms", category=category)
        t4 = Topping.objects.create(name="Onions", category=category)
        toppings = Topping.objects.all()
        assert toppings.count() == 4