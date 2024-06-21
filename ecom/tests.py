from django.contrib.auth.models import User
from django.test import TestCase

from ecom.models import Cart, Product, SquareToken


class SquareTokenModelTests(TestCase):
    def test_get_and_set_access_token(self):
        """Succeeds if an arbitrary access token can be saved and retrieved."""
        unencrypted_access_token = "super_secure_access_token"
        test_user = User.objects.create_user(
            username="test_user",
            email="test_user@domain.com",
            password="test_password",
        )
        test_token = SquareToken.objects.create(user=test_user)

        test_token.access_token = unencrypted_access_token

        # Fails if the access token was incorrectly encrypted
        self.assertNotEqual(test_token._access_token, unencrypted_access_token)
        # Fails if the access token was incorrectly decrypted
        self.assertEqual(test_token.access_token, unencrypted_access_token)

    def test_get_and_set_refresh_token(self):
        """Succeeds if an arbitrary refresh token can be saved and retrieved."""
        unencrypted_refresh_token = "super_secure_refresh_token"
        test_user = User.objects.create_user(
            username="test_user",
            email="test_user@domain.com",
            password="test_password",
        )
        test_token = SquareToken.objects.create(user=test_user)

        test_token.refresh_token = unencrypted_refresh_token

        # Fails if the refresh token was incorrectly encrypted
        self.assertNotEqual(test_token._refresh_token, unencrypted_refresh_token)
        # Fails if the refresh token was incorrectly decrypted
        self.assertEqual(test_token.refresh_token, unencrypted_refresh_token)


class CartModelTests(TestCase):
    def test_add_products_to_cart(self):
        """Succeeds if products are successfully added to a cart."""
        test_user = User.objects.create_user(
            username="test_user",
            email="test_user@domain.com",
            password="test_password",
        )
        test_product_1 = Product.objects.create(name="test_product_1", price=1.00)
        test_product_2 = Product.objects.create(name="test_product_2", price=2.00)

        test_cart = Cart.objects.create(user=test_user)

        test_cart.add_product(product_id=test_product_1.id, quantity=1)
        test_cart.add_product(product_id=test_product_2.id, quantity=2)

        # Fails if cartitem_set wasn't created
        self.assertIsNot(test_cart.cartitem_set.all(), None)
