from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsTests(TestCase):

    def setUp(self):
        address = Address.objects.create(number=4, street="my street",
                                        city="in city", state="room",
                                        zip_code=12345, country_iso_code="RSM")
        letting = Letting.objects.create(title="setUp", address_id=1)

    def test_200_status_code(self):
        response = self.client.get(reverse("lettings:index"))
        return self.assertEqual(response.status_code, 200)
