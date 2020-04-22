from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Item(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="items"
    )
    small_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    large_price = models.DecimalField(max_digits=5, decimal_places=2)
    toppings_allowed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category} - {self.name}"


class Topping(models.Model):
    name = models.CharField(max_length=64, null=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="toppings",
    )

    def __str__(self):
        return f"{self.category} - {self.name}"