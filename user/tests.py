from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):
    def test_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'masudrana',
            email = 'masud@example.com',
            password = 'testpass123'
            
        )
        self.assertEqual(user.username,'masudrana')
        self.assertEqual(user.email,'masud@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        admin_user = get_user_model()
        super_admin = admin_user.objects.create_superuser(
            username='superadmin',
            email = 'superadmin@example.com',
            password = 'testpass124'
        )
        self.assertEqual(super_admin.username,'superadmin')
        self.assertEqual(super_admin.email,'superadmin@example.com')
        self.assertTrue(super_admin.is_staff)
        self.assertTrue(super_admin.is_superuser)
        self.assertTrue(super_admin.is_active)