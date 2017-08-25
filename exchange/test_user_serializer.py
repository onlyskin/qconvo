from django.test import TestCase
from django.contrib.auth.models import User

from exchange.models import Language
from exchange.models import Link

from user_serializer import UserSerializer

class UserSerializerTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user(username='onlyskin', password='password');
        u.profile.name = 'sam'
        u.save()
        l1 = Language(name='english')
        l2 = Language(name='italian')
        l1.save()
        l2.save()
        Link(profile=u.profile, language=l1, level='n').save()
        Link(profile=u.profile, language=l2, level='b').save()
        self.u = u

    def test_returns_dict(self):
        serializer = UserSerializer()
        output = serializer.serialize(self.u)
        self.assertEqual(output['username'], 'onlyskin')
        self.assertEqual(output['name'], 'sam')
        self.assertEqual(output['native'][0], 'english')
        self.assertEqual(output['learning'][0], 'italian')

