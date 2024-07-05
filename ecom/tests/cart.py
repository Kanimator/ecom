from django.contrib.auth.models import User
from django.test import TestCase

from ecom.models.cart import Cart, CartItem
from ecom.models.order import Order, OrderItem
from ecom.models.product import Product


class CartModelTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="test_user", password="test_pass", email="example@crimsonslate.com"
        )
        self.test_cart = Cart.objects.create(user=self.test_user)
        self.test_product_1 = Product.objects.create(
            name="Test Product 1",
            desc="",
            visibility="VIS",
            price=10.00,
        )
        self.test_product_2 = Product.objects.create(
            name="Test Product 2",
            desc="",
            visibility="VIS",
            price=20.00,
        )

    def test_add_product_method(self) -> None:
        self.test_cart.add_product(product_id=self.test_product_1.id, quantity=-1)
