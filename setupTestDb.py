# run python manage.py flush to clear the db then run this script to populate
# it with random data

import os, django, random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qconvo.settings")
django.setup()

from django.contrib.auth.models import User

from exchange.models import Language
from exchange.models import Link

languages = ['english', 'polish', 'italian', 'japanese', 'spanish']
countries = ['United Kingdom', 'Poland', 'Italy', 'Japan', 'Spain']

with open('sample_names', 'r') as f:
    names = f.read().split('\n')
    random.shuffle(names)
    
with open('sample_words', 'r') as f:
    usernames = f.read().split('\n')
    random.shuffle(usernames)

def make_random_username():
    return usernames.pop()

def make_random_name():
    return names.pop()

def make_user(username, name, country, age):
    u = User.objects.create_user(username=username, password='p')
    u.profile.name = name
    u.profile.country = country
    u.profile.age = age
    u.save()
    natives = []
    natives.append(get_language(random.choice(languages)))
    learning = get_language(random.choice(languages))
    while natives[0] == learning:
        learning = get_language(random.choice(languages))
    u.profile.nativelangs.add(natives[0])
    Link(profile=u.profile, language=learning, level='b').save()
    u.save()

def make_language(name):
    language = Language(name=name)
    language.save()

def get_language(name):
    return Language.objects.get(name=name)

if __name__ == '__main__':
    [make_language(language) for language in languages]
    for i in range(100):
        username = make_random_username()
        name = make_random_name()
        country = random.choice(countries)
        age = random.randint(0, 99)
        make_user(username, name, country, age)
