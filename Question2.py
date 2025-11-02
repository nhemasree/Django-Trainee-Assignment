# Yes, by default signals run in the same thread as the caller.

# signals_test/app/signals.py

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def thread_checker(sender, instance, **kwargs):
    print("Signal Thread ID:", threading.get_ident())


# signals_test/manage.py shell

from django.contrib.auth.models import User
import threading

print("Caller Thread ID:", threading.get_ident())
User.objects.create(username="hema")