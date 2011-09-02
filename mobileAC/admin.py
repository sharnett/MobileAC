from mobileAC.models import Switch, AC, Thermometer, ThermoReading
from django.contrib import admin

class ReadingInline(admin.TabularInline):
    model = ThermoReading
    extra = 5

class ThermometerAdmin(admin.ModelAdmin):
    inlines = [ReadingInline]

admin.site.register(AC)
admin.site.register(Thermometer, ThermometerAdmin)
