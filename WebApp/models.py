from django.db import models

# Create your models here.
class SavedTweet(models.Model):
    tweet_text = models.CharField(max_length=200)