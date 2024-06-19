from django.contrib.auth.models import User
from django.test import TestCase

from ecom.models import SquareToken


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
