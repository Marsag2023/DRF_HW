import stripe
from config.settings import STRIPE_SECRET_KEY
# from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_SECRET_KEY


def create_stripe_product(instance):
    """Создаем stripe продукт"""
    title_product = f"{instance.well}" if instance.well else instance.lesson
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


# def  convert_rub_to_dollars(amount):
#     """Конвертируем рубли в доллары."""
#     c = CurrencyRates(amount)
#     rate = c.get_rate('RUB', 'USD')
#     return int(amount * rate)

def create_stripe_price(amount, product):
    """Создаем stripe цену"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount*100,
        product=product,
    )
    return price


def create_stripe_session(price):
    """ Создаем сессию оплаты в стра��пе """
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
