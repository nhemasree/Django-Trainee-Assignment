 """
 By default, Django signals are executed synchronously.
 That means the caller waits until all connected signal handlers have 
 finished executing before proceeding.
 """

 # signals_test/app/signals.py

 import time
 from django.db.models.signals import post_save
 from django.dispatch import receiver
 from django.contrib.auth.models import User


 @receiver(post_save, sender=User)
 def slow_signal(sender, instance, **kwargs):
     print("Signal handler started...")
     time.sleep(5)
     print("Signal handler finished!")


# signals_test/manage.py shell

from django.contrib.auth.models import User
import time

start = time.time()
User.objects.create(username="john")  # This triggers post_save
end = time.time()

print(f"Total time: {end - start:.2f} seconds")
