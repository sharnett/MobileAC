from django.db import models
from Remote_AC import max

class Switch(models.Model):
    IsOn = models.BooleanField()
    def save(self, *args, **kwargs):
        super(Switch, self).save(*args, **kwargs)
        print max(self.IsOn)
