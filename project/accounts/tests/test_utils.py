import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.http import Http404
from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.test import TestCase
from project.accounts.utils import get_account
from project.core.settings import BASE_DIR


class BaseTestCase(TestCase):
    """Base test class to set up test cases"""

    def setUp(self) -> None:
        user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com", password="password123"
        )
        self.test_profile, _created = Profile.objects.update_or_create(
            user=user,
            defaults={
                "first_name": "Test",
                "last_name": "User",
                "about_me": "About Me",
            },
        )


class GetAccountTest(BaseTestCase):

    def test_get_account_by_user(self):
        """Test get_account function with user parameter"""
        result = get_account(user=self.test_profile.user)
        self.assertEqual(result, self.test_profile)

    def test_get_account_by_pk(self):
        """Test get_account function with pk parameter"""
        result = get_account(pk=self.test_profile.pk)
        self.assertEqual(result, self.test_profile)

    def test_get_account_by_username(self):
        """Test get_account function with username parameter"""
        result = get_account(username=self.test_profile.user.username)
        self.assertEqual(result, self.test_profile)

    def test_get_account_invalid_parameters(self):
        """Test get_account function with invalid parameters"""
        with self.assertRaises(Http404):
            get_account()

    def test_get_account_not_found(self):
        """Test get_account function with non-existent parameters"""
        with self.assertRaises(Http404):
            get_account(username='nonexistentuser')