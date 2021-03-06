from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    country = models.ForeignKey('Country', null=True)
    age = models.IntegerField(null=True)
    nativelangs = models.ManyToManyField('Language',
        related_name='nativeprofiles')
    learninglangs = models.ManyToManyField('Language', through='Link',
        related_name='learningprofiles')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Language(models.Model):
    name = models.CharField(max_length=100)

class Country(models.Model):
    name = models.CharField(max_length=200)

LEVELCHOICE = (
    ('b', 'beginner'),
    ('e', 'elementary'),
    ('p', 'pre-intermediate'),
    ('i', 'intermediate'),
    ('u', 'upper-intermediate'),
    ('a', 'advanced'),
)

class Link(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    level = models.CharField(max_length=1, choices=LEVELCHOICE)
