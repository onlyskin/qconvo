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
        serializer = UserSerializer()
        output = serializer.serialize(user)
        self.assertEqual(output['username'], 'onlyskin')
        self.assertEqual(output['name'], 'sam')

