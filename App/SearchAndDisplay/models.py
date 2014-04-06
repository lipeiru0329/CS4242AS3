from django.db import models
from djangotoolbox.fields import ListField
from django.utils.encoding import smart_unicode

class ExpertUser(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    id_str = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    profile_image_url = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    
    def __unicode__(self):
        return smart_unicode(self.name)