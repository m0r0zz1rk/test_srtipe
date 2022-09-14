from django.db import models

from pay.stripe import CreateStripeProduct, CreateStripePriceForProduct


class Item(models.Model):
    """Модель товаров"""
    name = models.CharField(max_length=100,
                            null=False,
                            blank=False,
                            verbose_name='Наименование товаара')
    description = models.TextField(max_length=1000,
                                   verbose_name='Описание товара')
    price = models.PositiveIntegerField(blank=False,
                                        null=False,
                                        verbose_name='Стоимость единицы товара')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Создание нового Product при сохранении нового товара"""
        stripe_prod = CreateStripeProduct(self.name)
        stripe_price = CreateStripePriceForProduct(self.price*100, stripe_prod)
        new = StripeProduct()
        new.product_id = stripe_prod
        new.price_id = stripe_price
        super(Item, self).save(*args, **kwargs)
        new.item_id = self.id
        new.save()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class StripeProduct(models.Model):
    """Модель Product для Stripe"""
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='Товар'
    )
    product_id = models.CharField(max_length=50, verbose_name='product_id')
    price_id = models.CharField(max_length=50, verbose_name='price_id')

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Stripe Product'
        verbose_name_plural = 'Stripe Products'
# Create your models here.
