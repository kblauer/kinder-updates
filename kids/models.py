from django.db import models

class Kid(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    postTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.last_name + " " + self.first_name)
    

