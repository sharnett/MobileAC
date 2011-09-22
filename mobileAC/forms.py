from django.forms.models import ModelForm
from django.forms import RadioSelect, TextInput, CharField
from mobileAC.models import AC

class ACUpdateForm(ModelForm):
    password = CharField(max_length=100)
    class Meta:
        model = AC
        fields = ('isOn', 'temperature', 'fanSpeed')
        widgets = {'isOn': RadioSelect, 'temperature': TextInput(attrs={'size':'1'}), 'fanSpeed': RadioSelect}
    def clean(self):
        cleaned_data = self.cleaned_data
        temp = cleaned_data.get("temperature")
        pw = cleaned_data.get("password")

        if temp and temp < 60 or temp > 90:
            msg = u"Temperature must be between 60 and 90"
            self._errors["temperature"] = self.error_class([msg])
            del cleaned_data["temperature"]

        if pw != 'tittyback':
            self._errors["password"] = self.error_class([u"wrong"])

        return cleaned_data
