from django.test import TestCase
from django.urls import reverse


class IndexTest(TestCase):
    """Tests de la view index."""

    def setUp(self):
        """Configuration commune pour à chaque test.

        Les class de tests étant scindé par view, la response est
        communes pour tous les tests de la class.
        L'appel se fait avant chacun des tests.
        """
        self.response = self.client.get(reverse("index"))

    def test_200_status_code(self):
        return self.assertEquals(self.response.status_code, 200)

    def test_title_in_response(self):
        expected_title = b"<title>Holiday Homes</title>"
        return self.assertContains(self.response, expected_title,
                                   status_code=200)

    def test_template_used(self):
        expected_template = "index.html"
        return self.assertTemplateUsed(self.response, expected_template)
