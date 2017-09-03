# run python manage.py flush to clear the db then run this script to populate
# it with random data

import os, django, random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qconvo.settings")
django.setup()

from django.contrib.auth.models import User

from exchange.models import Language
from exchange.models import Link

languages = ['english', 'polish', 'italian', 'japanese', 'spanish']
numbers = range(1000)
random.shuffle(numbers)

def make_random_username():
    return 'user' + str(numbers.pop())

def make_random_name():
    return 'name' + str(numbers.pop())

def make_user(username, name, native_lang, learning_lang):
    u = User.objects.create_user(username=username, password='p')
    u.profile.name = name
    u.save()
    u.profile.nativelangs.add(native_lang)
    Link(profile=u.profile, language=learning_lang, level='b').save()
    u.save()

def make_language(name):
    language = Language(name=name)
    language.save()

def get_language(name):
    return Language.objects.get(name=name)

if __name__ == '__main__':
    [make_language(language) for language in languages]
    for i in range(500):
        username = make_random_username()
        name = make_random_name()
        native = random.choice(languages)
        learning = random.choice(languages)
        while native == learning:
            learning = random.choice(languages)
        make_user(username, name, get_language(native), get_language(learning))
