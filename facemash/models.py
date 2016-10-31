from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
@python_2_unicode_compatible
class Image(models.Model):
    serial_no = models.IntegerField()
    image = models.CharField(max_length=200)
    point = models.IntegerField(default=0)
    def __str__(self):
        return self.image
    
    class Meta:
        db_table = 'pictures'
    
