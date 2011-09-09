from django.db import models
from math import floor, ceil
#from Remote_AC import max, max2

class Switch(models.Model):
    isOn = models.BooleanField(verbose_name='Power', choices=((True,'on'), (False,'off')))
    name = models.CharField(max_length=30)
    def save(self, *args, **kwargs):
        super(Switch, self).save(*args, **kwargs)
        #if max(self.isOn): print "it worked"
        #else: print "it failed"
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "switches"

class AC(Switch):
    temperature = models.IntegerField()
    fanSpeed = models.IntegerField(verbose_name='Fan Speed', default=1, choices=((1,'lo'), (2,'med'), (3,'hi')))
    def save(self, *args, **kwargs):
        super(AC, self).save(*args, **kwargs)
        #print max2(self)
    class Meta:
        verbose_name = "AC"
        verbose_name_plural = "ACs"

class Thermometer(models.Model):
    AC = models.ForeignKey(AC)
    name = models.CharField(max_length=12)
    def __unicode__(self):
        return self.name
    def googleGraph(self):
        n = 40 # number of readings to graph
        readings = self.thermoreading_set.all()[:n]
        temps = [float(reading.temperature) for reading in readings]
        hums = [float(reading.humidity) for reading in readings]
        temps.reverse()
        hums.reverse()

        # scaling bullshit
        tempMin, tempMax, humMin, humMax = [min(temps), max(temps), min(hums), max(hums)]
        tempMin = 10*floor(.1*tempMin)
        humMin = 10*floor(.1*humMin)
        tempMax = 10*ceil(.1*tempMax)
        humMax = 10*ceil(.1*humMax)
        temps = ','.join([str(99*(temp - tempMin)/(tempMax - tempMin)) for temp in temps])
        hums = ','.join([str(99*(hum - humMin)/(humMax - humMin)) for hum in hums])
        
        src = '''
        "http://chart.apis.google.com/chart
        ?chxl=0:|-3hr|-2hr|-1hr|Now|1:|%d%%|%d%%|2:|%d&deg;|%d&deg;
        &chxp=0,0,34,68,100
        &chxs=0,00AA00,13.333,0.5,l,676767|2,676767,10.833,0,l,676767
        &chxt=x,r,y
        &chs=250x168
        &cht=lc
        &chco=FF0000,0000FF
        &chds=0,100,0,100
        &chd=t:%s|%s
        &chdl=Temperature+(&deg;F)|%%25+Humidity
        &chdlp=b
        &chg=34,0,0,0
        &chma=|4
        &chtt=Current+Conditions"''' % (tempMin, tempMax, humMin, humMax, temps, hums)
        src = ''.join(src.split())
        myUrl = '''<img src=%s width="250" height="168" alt="Current Conditions" />''' % src
        return myUrl

class ThermoReading(models.Model):
    thermometer = models.ForeignKey(Thermometer)
    time = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    humidity = models.DecimalField(max_digits=5, decimal_places=1)
    def __unicode__(self):
        return "temp: %5.1f hum: %5.1f" % (self.temperature, self.humidity)
    class Meta:
        ordering = ['-time']
