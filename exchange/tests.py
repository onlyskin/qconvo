from django.test import TestCase
from django.contrib.auth.models import User

from exchange.models import Language, Country, Link

class ExchangeViewsTestCase(TestCase):
    def make_user(self, username, name, native_lang, learning_lang, country, age):
        u = User.objects.create_user(username=username, password='p')
        u.profile.name = name
        u.profile.country = country
        u.profile.age = age
        u.save()
        u.profile.nativelangs.add(native_lang)
        Link(profile=u.profile, language=learning_lang, level='b').save()
        u.save()

    def make_language(self, name):
        language = Language(name=name)
        language.save()
        return language

    def make_country(self, name):
        country = Country(name=name)
        country.save()
        return country

    def setUp(self):
        english = self.make_language('english')
        italian = self.make_language('italian')
        polish = self.make_language('polish')
        unitedKingdom = self.make_country('United Kingdom')
        poland = self.make_country('Poland')
        self.make_user('onlyskin', 'sam', english, polish, unitedKingdom, 26)
        self.make_user('Asia', 'Joanna', polish, english, poland, 28)
        self.make_user('Jan', 'J', polish, italian, poland, 15)

    def test_index(self):
        resp = self.client.get('/exchange/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('qconvo' in resp.content)
        self.assertTrue('<body>' in resp.content)

    def api_profiles_returns_users(self):
        resp = self.client.get('/exchange/api/profiles?n=polish&l=english')
        self.assertEqual(resp.status_code, 200)
        user_data = resp.json()
        self.assertEqual(len(user_data), 1)
        self.assertEqual('Joanna', user_data[0]['name'])
        self.assertEqual(['polish'], user_data[0]['native'])
        self.assertEqual(['english'], user_data[0]['learning'])
        self.assertEqual('Poland', user_data[0]['country'])
        self.assertEqual(28, user_data[0]['age'])

    def api_profiles_returns_empty_list_when_bad_langs(self):
        resp = self.client.get('/exchange/api/profiles?n=INVALID&l=INVALID')
        self.assertEqual(resp.status_code, 200)
        user_data = resp.json()
        self.assertEqual([], user_data)

    def test_languages(self):
        resp = self.client.get('/exchange/api/languages/')
        self.assertEqual(resp.status_code, 200)
        languages = resp.json()
        self.assertTrue('english' in languages)

    def test_countries(self):
        resp = self.client.get('/exchange/api/countries/')
        self.assertEqual(resp.status_code, 200)
        countries = resp.json()
        self.assertTrue('United Kingdom' in countries)

    def test_profile(self):
        self.client.login(username='onlyskin', password='p')
        resp = self.client.get('/exchange/api/profile')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual('sam', data['name'])
        self.assertEqual(26, data['age'])
        self.assertEqual('United Kingdom', data['country'])
        self.assertEqual('english', data['native'][0])
        self.assertEqual('polish', data['learning'][0]['name'])
        self.assertEqual('b', data['learning'][0]['level'])

