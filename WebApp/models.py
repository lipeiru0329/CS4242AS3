from django.db import models
from jsonfield import JSONField

# Create your models here.
class SavedTweet(models.Model):
    json = JSONField()