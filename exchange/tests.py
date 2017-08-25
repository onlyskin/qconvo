from django.test import TestCase
from django.contrib.auth.models import User

from exchange.models import Language
from exchange.models import Link

class ExchangeViewsTestCase(TestCase):
    def setUp(self):
        u0 = User.objects.create_user(username='onlyskin', password='password');
        u0.profile.name = 'sam'
        u0.save()
        u1 = User.objects.create_user(username='Asia', password='password');
        u1.profile.name = 'Joanna'
        u1.save()
        l1 = Language(name='english')
        l2 = Language(name='italian')
        l3 = Language(name='polish')
        l1.save()
        l2.save()
        l3.save()
        Link(profile=u0.profile, language=l1, level='n').save()
        Link(profile=u0.profile, language=l2, level='b').save()
        Link(profile=u1.profile, language=l3, level='n').save()
        Link(profile=u1.profile, language=l1, level='b').save()

    def test_index(self):
        resp = self.client.get('/exchange/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('qconvo' in resp.content)

    def test_users(self):
        resp = self.client.get('/exchange/api/users/polish/english')
        self.assertEqual(resp.status_code, 200)
        user_data = resp.json()[0]
        self.assertEqual(user_data['username'], 'Asia')
        self.assertEqual(user_data['name'], 'Joanna'),
        self.assertEqual(user_data['native'], ['polish']),
        self.assertEqual(user_data['learning'], ['english']),

    def test_languages(self):
        resp = self.client.get('/exchange/api/languages/')
        self.assertEqual(resp.status_code, 200)
        languages = resp.json()
        self.assertTrue('english' in languages)
