from django.test import TestCase
from django.contrib.auth.models import User

from exchange.models import Language
from exchange.models import Link

class ExchangeViewsTestCase(TestCase):
    fixtures = ['test_data.json']

    def setUp(self):
        u = User.objects.get(username='onlyskin')
        u.profile.name = 'sam'
        u.save()
        l1 = Language.objects.get(name='english')
        l2 = Language.objects.get(name='italian')
        Link(profile=u.profile, language=l1, level='n').save()
        Link(profile=u.profile, language=l2, level='b').save()

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
        self.assertEqual(user_data['native'], ['english']),
        self.assertEqual(user_data['learning'], ['italian']),

    def test_languages(self):
        resp = self.client.get('/exchange/api/languages/')
        self.assertEqual(resp.status_code, 200)
        languages = resp.json()
        self.assertTrue('english' in languages)
