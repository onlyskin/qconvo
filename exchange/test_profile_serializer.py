from django.test import TestCase
from django.contrib.auth.models import User

from exchange.models import Language, Country, Link, Profile

from profile_serializer import ProfileSerializer

class ProfileSerializerTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user(username='u', password='p')
        p = u.profile
        p.name = 'sam'
        c = Country(name='United Kingdom')
        c.save()
        p.country = c
        p.age = 25
        p.save()
        l1 = Language(name='english')
        l2 = Language(name='italian')
        l1.save()
        l2.save()
        p.nativelangs.add(l1)
        Link(profile=p, language=l2, level='b').save()
        p.save()
        self.p = p

    def test_returns_dict(self):
        serializer = ProfileSerializer()
        output = serializer.serialize(self.p)
        self.assertEqual(output['name'], 'sam')
        self.assertEqual(output['country'], 'United Kingdom')
        self.assertEqual(output['age'], 25)
        self.assertEqual(output['native'][0], 'english')
        self.assertEqual(output['learning'][0], 'italian')

