from django.test import TestCase
from django.urls import reverse

class ContactURLsTest(TestCase):
    def test_contact_index_url_is_correct(self):
        url = reverse('contact:index')
        self.assertEqual(url, '/')