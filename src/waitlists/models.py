from django.db import models


class WaitlistEntry(models.Model):
    email = models.EmailField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    