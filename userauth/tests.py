from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from userauth.models import User

class AuthFlowTests(APITestCase):
    def setUp(self):
        self.email = "demo@test.com"
        self.password = "TestPass123"

    def test_register_verify_login(self):
        # Register user
        r = self.client.post(reverse("register"), {
            "email": self.email,
            "username": "demo",
            "first_name": "Demo",
            "last_name": "User",
            "user_type": "student",
            "password": self.password
        }, format="json")
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        otp = r.data.get("otp")
        self.assertIsNotNone(otp)

        # Verify OTP
        v = self.client.post(reverse("verify-otp"), {
            "email": self.email,
            "otp": otp
        }, format="json")
        self.assertEqual(v.status_code, status.HTTP_200_OK)

        # Login
        l = self.client.post(reverse("login"), {
            "email": self.email,
            "password": self.password
        }, format="json")
        self.assertEqual(l.status_code, status.HTTP_200_OK)
        self.assertIn("access", l.data)
        self.assertIn("refresh", l.data)

        # Access profile
        token = l.data["access"]
        p = self.client.get(reverse("profile"), HTTP_AUTHORIZATION=f"Bearer {token}")
        self.assertEqual(p.status_code, status.HTTP_200_OK)
