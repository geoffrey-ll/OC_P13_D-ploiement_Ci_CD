from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsIndexTest(TestCase):
    """Tests de la view index."""

    @classmethod
    def setUpTestData(cls):
        """Configuration commune et initiale pour la class.

        La DB de test doit rester non modifié par les tests, car appeler
        la méthode n'est appelé qu'une seule fois pour l'ensemble des
        tests de la class.
        """
        cls.address = Address.objects.create(
            number=4, street="my street", city="in city", state="room",
            zip_code=12345, country_iso_code="RSM")
        cls.letting = Letting.objects.create(title="A letting",
                                             address=cls.address)

    def setUp(self):
        """Configuration commune pour à chaque test.

        Les class de tests étant scindé par view, la response est
        communes pour tous les tests de la class.
        L'appel se fait avant chacun des tests.
        """
        self.response = self.client.get(reverse("lettings:index"))

    def test_200_status_code(self):
        return self.assertEqual(self.response.status_code, 200)

    def test_title_in_response(self):
        expected_title = b"<title>Lettings</title>"
        return self.assertContains(self.response, expected_title,
                                   status_code=200)

    def test_template_used(self):
        expected_template = "lettings/index.html"
        return self.assertTemplateUsed(self.response, expected_template)


class LettingsLettingTest(TestCase):
    """Tests de la view letting."""

    @classmethod
    def setUpTestData(cls):
        """Configuration commune et initiale pour la class.

        La DB de test doit rester non modifié par les tests, car appeler
        la méthode n'est appelé qu'une seule fois pour l'ensemble des
        tests de la class.
        """
        cls.address = Address.objects.create(
            number=4, street="my street", city="in city", state="room",
            zip_code=12345, country_iso_code="RSM")
        cls.letting = Letting.objects.create(title="A letting",
                                             address=cls.address)

    def setUp(self):
        """Configuration commune pour à chaque test.

        Les class de tests étant scindé par view, la response est
        communes pour tous les tests de la class.
        L'appel se fait avant chacun des tests.
        """
        self.response = self.client.get(reverse("lettings:letting",
                                                args=[self.letting.id]))

    def test_200_status_code(self):
        return self.assertEqual(self.response.status_code, 200)

    def test_title_in_response(self):
        expected_title = f"<title>{self.letting.title}</title>".encode()
        return self.assertContains(self.response, expected_title,
                                   status_code=200)

    def test_template_used(self):
        expected_template = "lettings/letting.html"
        return self.assertTemplateUsed(self.response, expected_template)
