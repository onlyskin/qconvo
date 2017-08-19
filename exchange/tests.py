from django.test import TestCase
from django.contrib.auth.models import User

class ExchangeViewsTestCase(TestCase):
    fixtures = ['test_data.json']

    def setUp(self):
        u = User.objects.get(username='onlyskin')
        u.profile.name = 'sam'
        u.save()

    def test_index(self):
        resp = self.client.get('/exchange/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('qconvo' in resp.content)

    def test_users(self):
        resp = self.client.get('/exchange/api/users/')
        self.assertEqual(resp.status_code, 200)
        user_data = resp.json()[0]
        self.assertEqual(user_data['username'], 'onlyskin')
        self.assertEqual(user_data['name'], 'sam'),

    def test_languages(self):
        resp = self.client.get('/exchange/api/languages/')
        self.assertEqual(resp.status_code, 200)
        languages = resp.json()
        self.assertTrue('english' in languages)
