from django.test import TestCase
from django.urls import reverse

class ContactURLsTest(TestCase):
    def test_contact_index_url_is_correct(self):
        url = reverse('contact:index')
        self.assertEqual(url, '/')
    
    def test_contact_search_url_is_correct(self):
        url = reverse('contact:search')
        self.assertEqual(url, '/search')
    
    def test_contact_id_url_is_correct(self):
        url = reverse('contact:contact', kwargs={"contact_id": 1})
        self.assertEqual(url, '/contact/1/')

    def test_contact_create_url_is_correct(self):
        url = reverse('contact:create')
        self.assertEqual(url, '/contact/create/')

    def test_contact_update_url_is_correct(self):
        url = reverse('contact:update', kwargs={'contact_id': 1})
        self.assertEqual(url, '/contact/1/update')

    def test_contact_delete_url_is_correct(self):
        url = reverse('contact:delete', kwargs={'contact_id': 1})
        self.assertEqual(url, '/contact/1/delete')

    def test_contact_create_user_url_is_correct(self):
        url = reverse('contact:register')
        self.assertEqual(url,'/user/create/')

    def test_contact_login_user_url_is_correct(self):
        url = reverse('contact:login')
        self.assertEqual(url, '/user/login/')

    def test_contact_logout_user_url_is_correct(self):
        url = reverse('contact:logout')
        self.assertEqual(url, '/user/logout/')
    
    def test_contact_user_update_url_is_correct(self):
        url = reverse('contact:user_update')
        self.assertEqual(url, '/user/update/')


    