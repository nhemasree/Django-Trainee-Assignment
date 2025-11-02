"""
Yes — by default Django signals run inside the same database transaction as
the caller (if any).
"""

# signals_test/app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def rollback_signal(sender, instance, **kwargs):
    print("Signal triggered! Raising error to test rollback...")
    raise Exception("Rolling back transaction!")

# signals_test/manage.py shell

from django.contrib.auth.models import User

try:
    User.objects.create(username="broken_user")
except Exception as e:
    print(e)

print("User exists?", User.objects.filter(username="broken_user").exists())