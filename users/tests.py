from datetime import timedelta
from http import HTTPStatus

from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.forms import EmailVerification
from users.models import User

if __name__ == "__main__":
    import unittest

    unittest.main()


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse("users:registration")
        self.data = {
            "first_name": "Daniel",
            "last_name": "Kotelnikov",
            "username": "Daniel",
            "email": "daniel@yandex.ru",
            "password1": "58523",
            "password2": "58523",
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Store - Регистрация")
        self.assertTemplateUsed(response, "users/registration.html")

    def test_user_registration_post(self):
        first_name = self.data["first_name"]
        self.assertFalse(User.objects.filter(first_name=first_name).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("users:login"))
        self.assertTrue(User.objects.filter(first_name=first_name).exists())

        email_verification = EmailVerification.objects.filter(
            first_name=first_name
        )
        self.assertEqual(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date(),
        )

    def test_user_registration_error(self):
        User.objects.create(first_name=self.data["first_name"])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "User has been created", html=True)


class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
            "Subject here",
            "Here is the message.",
            "storeserverlogin@yandex.ru",
            ["daniel.kotelnickov@yandex.ru"],
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, "Subject here")
