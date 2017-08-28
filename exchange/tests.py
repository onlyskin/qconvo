from django.test import TestCase
from django.contrib.auth.models import User

from exchange.models import Language
from exchange.models import Link

class ExchangeViewsTestCase(TestCase):
    def make_user(self, username, name, native_lang, learning_lang):
        u = User.objects.create_user(username=username, password='p')
        u.profile.name = name
        u.save()
        u.profile.nativelangs.add(native_lang)
        Link(profile=u.profile, language=learning_lang, level='b').save()
        u.save()

    def make_language(self, name):
        language = Language(name=name)
        language.save()
        return language

    def setUp(self):
        english = self.make_language('english')
        italian = self.make_language('italian')
        polish = self.make_language('polish')
        self.make_user('onlyskin', 'sam', english, polish)
        self.make_user('Asia', 'Joanna', polish, english)
        self.make_user('Jan', 'J', polish, italian)

    def test_index(self):
        resp = self.client.get('/exchange/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('qconvo' in resp.content)

    def test_profiles(self):
        resp = self.client.get('/exchange/api/profiles?n=polish&l=english')
        self.assertEqual(resp.status_code, 200)
        user_data = resp.json()
        self.assertEqual(len(user_data), 1)
        self.assertEqual('Joanna', user_data[0]['name']),
        self.assertEqual(['polish'], user_data[0]['native']),
        self.assertEqual(['english'], user_data[0]['learning']),

    def test_languages(self):
        resp = self.client.get('/exchange/api/languages/')
        self.assertEqual(resp.status_code, 200)
        languages = resp.json()
        self.assertTrue('english' in languages)
