from django.contrib.auth.models import User
from django.db import models


class Feedback(models.Model):
    feedbackText = models.TextField()
    postTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    sentByParent = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.id)