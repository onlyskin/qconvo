from django.test import TestCase

class ExchangeViewsTestCase(TestCase):
    fixtures = ["exchanges_views_testdata.json"]

    def test_index(self):
        resp = self.client.get('/exchange/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("qconvo" in resp.content)

    def test_users(self):
        resp = self.client.get('/exchange/api/users/')
        self.assertEqual(resp.status_code, 200)
        user_data = resp.json()[0]['fields']
        self.assertEqual(user_data['username'], "sam")
        # self.assertEqual(set(user_data['languages']),
        #     set('japanese', 'italian'))
