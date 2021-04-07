from django.db.models.signals import pre_save
from django.contrib.auth.models import User

"""
We want to login with the user's email, not username.
For this, we can override Django's default User model or do this quickfix using a signal.

"""

def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email

pre_save.connect(updateUser, sender=User)