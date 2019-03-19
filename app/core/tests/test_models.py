from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test creating a new user with an email address is successful"""
        email = 'test@emptycircle.net'
        password = 'PassPassTest789'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EMPTYCIRCLE.NET'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())