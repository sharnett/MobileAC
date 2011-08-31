from django.db import models
from Remote_AC import max, max2

class Switch(models.Model):
    isOn = models.BooleanField(verbose_name='Power', choices=((True,'on'), (False,'off')))
    name = models.CharField(max_length=30)
    def save(self, *args, **kwargs):
        super(Switch, self).save(*args, **kwargs)
        if max(self.isOn): print "it worked"
        else: print "it failed"
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "switches"

class AC(Switch):
    temperature = models.IntegerField()
    fanSpeed = models.IntegerField(verbose_name='Fan Speed', default=1, choices=((1,'lo'), (2,'med'), (3,'hi')))
    def save(self, *args, **kwargs):
        super(AC, self).save(*args, **kwargs)
        print max2(self)
    class Meta:
        verbose_name = "AC"
        verbose_name_plural = "ACs"
