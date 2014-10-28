from django.db import models

class Update(models.Model):
    updateText = models.TextField()
    postTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.id)
    

