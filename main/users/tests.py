from django.test import TestCase
from users.models import CustomUser, Profile


class CustomUserModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="test_user",
            email="test@example.com",
            password="password123"
        )

    def test_user_creation(self):
        """Test that a user instance can be created"""
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(self.user.username, "test_user")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("password123"))

    def test_user_string_representation(self):
        """Test that the string representation of the user is correct"""
        self.assertEqual(str(self.user), "test_user")

    def test_profile_creation(self):
        """Test that a profile is created upon user creation"""
        self.assertIsNotNone(self.user.profile)
