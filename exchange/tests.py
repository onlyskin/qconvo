from django.test import TestCase

class ExchangeViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/exchange/users/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['message'], 'Hello World')
