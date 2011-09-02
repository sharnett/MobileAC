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

class Thermometer(models.Model):
    AC = models.ForeignKey(AC)
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class ThermoReading(models.Model):
    thermometer = models.ForeignKey(Thermometer)
    time = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    humidity = models.DecimalField(max_digits=5, decimal_places=1)
    def __unicode__(self):
        return "temp: %5.1f hum: %5.1f" % (self.temperature, self.humidity)
