from django.test import TestCase

from user_serializer import UserSerializer

class Container():
    pass

class UserSerializerTestCase(TestCase):

    def test_returns_dict(self):
        user = Container()
        user.username = 'onlyskin'
        user.profile = Container()
        user.profile.name = 'sam'
        user.profile.language_set = Container()
        user.profile.language_set.all = lambda: [Container().name = 'english']

        serializer = UserSerializer()
        output = serializer.serialize(user)
        self.assertEqual(output['username'], 'onlyskin')
        self.assertEqual(output['name'], 'sam')
        self.assertEqual(output['languages'][0]['name'] = 'english')

