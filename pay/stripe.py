import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET


def CreateStripeSessionService(price_id=None, quantity=1):
    """Создание Stripe Session ID для оплаты выбранного товара"""
    session = stripe.checkout.Session.create(
            cancel_url="https://stripe.coko38.ru",
            success_url="https://stripe.coko38.ru",
            line_items=[
                {
                    "price": price_id,
                    "quantity": quantity
                },
            ],
            mode="payment",
        )
    return session


def CreateStripeProduct(name):
    """Создание нового Stripe Product"""
    product = stripe.Product.create(name=name)
    return product['id']


def CreateStripePriceForProduct(price, product_id):
    """Создание цены для Stripe Product"""
    price = stripe.Price.create(
        unit_amount=price,
        currency="rub",
        product=product_id,
    )
    return price['id']
