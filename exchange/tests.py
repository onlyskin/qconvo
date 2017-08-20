from django.test import TestCase
from django.contrib.auth.models import User

from exchange.models import Language
from exchange.models import Level
from exchange.models import Link

class ExchangeViewsTestCase(TestCase):
    fixtures = ['test_data.json']

    def setUp(self):
        u = User.objects.get(username='onlyskin')
        u.profile.name = 'sam'
        u.save()
        language = Language.objects.get(name='english')
        level = Level.objects.get(tag='native')
        l = Link(profile=u.profile, language=language, level=level)
        l.save()

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
        self.assertEqual(user_data['languages'][0]['language'], 'english')
        self.assertEqual(user_data['languages'][0]['level'], 'native')

    def test_languages(self):
        resp = self.client.get('/exchange/api/languages/')
        self.assertEqual(resp.status_code, 200)
        languages = resp.json()
        self.assertTrue('english' in languages)
