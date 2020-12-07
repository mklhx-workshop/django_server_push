import json
from django.db import models
from django.utils import timezone
from tastypie.utils.timezone import now

# Create your models here.

class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField()
    subscription_info = models.TextField()

    def __str__(self):
        return json.loads(self.subscription_info)
    