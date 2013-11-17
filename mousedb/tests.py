"""This file contains tests for the root application.

These tests will verify function of the home and logout views.
"""

from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.contrib.auth.models import User

class RootViewTests(TestCase):
    """These are tests for the root views.  Included are tests for home and logout."""
    fixtures = ['test_breeding', 'test_animals', 'test_strain']

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user('blah', 'blah@blah.com', 'blah')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.client.login(username='blah', password='blah')
        self.factory = RequestFactory()

    def tearDown(self):
        self.client.logout()
        self.test_user.delete()

    def test_home(self):
        """This test checks the view which displays the home page.  It checks for the correct templates and status code."""        
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'home.html')

    def test_logout(self):
        """This test checks the view which displays the logout page.  It checks for the correct templates and status code."""        
        response = self.client.get('/accounts/logout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logged_out.html')
        self.assertTemplateUsed(response, 'admin/base.html')
        self.assertTemplateUsed(response, 'admin/base_site.html')
  
    def test_login(self):
        """This test checks the view which displays the login page.  It checks for the correct templates and status code."""        
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertTemplateUsed(response, 'jquery_script.html')
        self.assertTemplateUsed(response, 'jquery_ui_script_css.html')
        self.assertTemplateUsed(response, 'menu_script.html')

    def test_api_view(self):
        """This test checks the view which displays the api keys.  It checks for the correct templates and status code."""        
        response = self.client.get('/api_key')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'api_key.html')
