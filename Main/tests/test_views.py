from django.test import TestCase    
from Main.views import home, copy, paste, preEdit, edit
from Main.models import MainModel
from django.urls import reverse

class MainViewTestCase(TestCase):

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_copy_view(self):
        object =  MainModel.objects.create(key='test_key', data='test_data')
        response = self.client.post(reverse('copy'), {'key': 'test_key'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'copy.html')
        self.assertContains(response, 'test_data')

    def test_paste_view(self):
        response = self.client.get(reverse('paste'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'paste.html')
        response = self.client.post(reverse('paste'), {'key': 'test_key', 'data': 'test_data'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MainModel.objects.count(), 1)
        response = self.client.post(reverse('paste'), {'key2': 'test_key', 'data': 'test_data'})
        self.assertEqual(response.status_code, 200)

    def test_preEdit_view(self):
        object =  MainModel.objects.create(key='test_key', data='test_data')
        response = self.client.post(reverse('preEdit'), {'key': 'test_key'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('edit'))
        response = self.client.post(reverse('preEdit'), {'key': 'test_key2', 'data': 'test_data'})
        self.assertTemplateUsed(response, 'copy.html')
        response = self.client.post(reverse('edit'), {'key': 'test_key', 'data': 'test_data'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MainModel.objects.count(), 1)
        self.assertEqual(MainModel.objects.get(key='test_key').data, 'test_data')


