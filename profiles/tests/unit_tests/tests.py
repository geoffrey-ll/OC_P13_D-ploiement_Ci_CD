"""Tests sur les vues de l'app profiles."""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


class ProfilesIndexTest(TestCase):
    """Tests de la view index."""

    @classmethod
    def setUpTestData(cls):
        """Configuration commune et initiale pour la class.

        La DB de test doit rester non modifié par les tests, car la
        méthode n'est appelée qu'une seule fois pour l'ensemble des
        tests de la class.
        """
        cls.user = User.objects.create(
            username="User tester", password="password", first_name="Only",
            last_name="Tester", email="email@email.com")
        cls.profile = Profile.objects.create(user=cls.user,
                                             favorite_city="World")

    def setUp(self):
        """Configuration commune pour à chaque test.

        Les class de tests étant scindé par view, la response est
        communes pour tous les tests de la class.
        L'appel se fait avant chacun des tests.
        """
        self.response = self.client.get(reverse("profiles:index"))

    def test_200_status_code(self):
        return self.assertEqual(self.response.status_code, 200)

    def test_title_in_response(self):
        expected_title = b"<title>Profiles</title>"
        return self.assertContains(self.response, expected_title,
                                   status_code=200)

    def test_template_used(self):
        expected_template = "profiles/index.html"
        return self.assertTemplateUsed(self.response, expected_template)


class ProfilesLettingTest(TestCase):
    """Tests de la view profile."""

    @classmethod
    def setUpTestData(cls):
        """Configuration commune et initiale pour la class.

        La DB de test doit rester non modifié par les tests, car la
        méthode n'est appelé qu'une seule fois pour l'ensemble des
        tests de la class.
        """
        cls.user = User.objects.create(
            username="User tester", password="password", first_name="Only",
            last_name="Tester", email="email@email.com")
        cls.profile = Profile.objects.create(user=cls.user,
                                             favorite_city="World")

    def setUp(self):
        """Configuration commune pour à chaque test.

        Les class de tests étant scindé par view, la response est
        communes pour tous les tests de la class.
        L'appel se fait avant chacun des tests.
        """
        self.response = self.client.get(reverse("profiles:profile",
                                                args=[self.user.username]))

    def test_200_status_code(self):
        return self.assertEqual(self.response.status_code, 200)

    def test_title_in_response(self):
        expected_title = \
            f"<title>{self.profile.user.username}</title>".encode()
        return self.assertContains(self.response, expected_title,
                                   status_code=200)

    def test_template_used(self):
        expected_template = "profiles/profile.html"
        return self.assertTemplateUsed(self.response, expected_template)
