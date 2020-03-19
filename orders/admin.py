from django.contrib import admin

from .models import Category, Item, Topping


class ItemInline(admin.StackedInline):
    model = Item


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)
admin.site.register(Topping)
