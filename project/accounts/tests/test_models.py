import os
from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

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


class ProfileModelTests(BaseTestCase):
    """A class to test Profile model"""

    def test_profile_creation(self):
        """Whether the fields of created Profile instance is correct"""

        self.assertEqual(self.test_profile.first_name, "Test")
        self.assertEqual(self.test_profile.last_name, "User")
        self.assertEqual(self.test_profile.about_me, "About Me")
        self.assertEqual(self.test_profile.full_name, "Test User")

    def test_profile_has_default_image_url(self):
        """Whether a profile has a default image"""

        self.assertEqual(
            self.test_profile.profile_image_url, "/static/img/no_image_md.png"
        )
        
    def test_profile_has_image_url_with_image_set(self):
        """Whether a profile has a set image"""
        image_path = os.path.join(BASE_DIR, 'accounts', 'tests', 'test_profile_image.png')
        with open(image_path, 'rb') as f:
            image_file = SimpleUploadedFile(name='test_profile_image.png', content=f.read(), content_type='image/png')
        self.test_profile.profile_image = image_file
        self.test_profile.save()
        actual_filename = os.path.basename(self.test_profile.profile_image.name)
        expected_image_url = f'/media/profile_uploads/{actual_filename}'

        self.assertEqual(self.test_profile.profile_image_url, expected_image_url)
    


class UserModelTest(TestCase):
    """A class to test Profile model"""

    def test_user_create_func_creates_profile(self):
        get_user_model().objects.create_user(
            username="testuser", email="test@test.com", password="password123"
        )
        self.assertEqual(Profile.objects.count(), 1)

    def test_superuser_create_func_creates_profile(self):
        get_user_model().objects.create_superuser(
            username="testuser", email="test@test.com", password="password123"
        )
        self.assertEqual(Profile.objects.count(), 1)
