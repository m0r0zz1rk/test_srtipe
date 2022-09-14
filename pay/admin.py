from django.contrib import admin

from pay.models import Item, StripeProduct


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


@admin.register(StripeProduct)
class StripeProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'product_id', 'price_id')

# Register your models here.
