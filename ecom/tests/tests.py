from django.contrib.auth.models import User
from django.test import TestCase

from ecom.models import Cart, Product

# How many lines can we get this file to?

class CartModelTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="test_user",
            email="test_user@domain.com",
            password="test_password",
        )
        self.test_cart = Cart.objects.create(user=self.test_user)

    def test_add_products_to_cart(self):
        """Succeeds if products are successfully added to the test cart."""
        test_product_1 = Product.objects.create(name="test_product_1", price=1.00)
        test_product_2 = Product.objects.create(name="test_product_2", price=2.00)

        self.test_cart.add_product(product_id=test_product_1.id, quantity=1)
        self.test_cart.add_product(product_id=test_product_2.id, quantity=2)

        self.assertIsNot(self.test_cart.items.all(), None)

    def test_rm_product_from_cart(self):
        """Succeeds if products are successfully removed from the test cart."""
        test_product_1 = Product.objects.create(name="test_product_1", price=1.00)
        test_product_2 = Product.objects.create(name="test_product_2", price=2.00)
        self.test_cart.add_product(product_id=test_product_1.id, quantity=1)
        self.test_cart.add_product(product_id=test_product_2.id, quantity=2)

        self.test_cart.rm_product(product_id=test_product_1.id, quantity=1)
        self.test_cart.rm_product(product_id=test_product_2.id, quantity=1)

        self.test_cart.save()

        self.assertIsNot(self.test_cart.items.all(), None)
