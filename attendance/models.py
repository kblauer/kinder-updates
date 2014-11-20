import datetime

from django.db import models
from django.utils import timezone

from kids.models import Kid


class Attendance(models.Model):
    attDate = models.DateField()
    didAtt = models.BooleanField(default=False)
    postTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    kid = models.ForeignKey(Kid)

    def __unicode__(self):
        return str(self.id)
    
