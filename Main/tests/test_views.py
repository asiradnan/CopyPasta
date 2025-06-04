from django.test import TestCase    
from Main.views import home, copy, paste, preEdit, edit

class MainViewTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

