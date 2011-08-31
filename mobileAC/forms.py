from django.forms.models import ModelForm
from django.forms import RadioSelect, TextInput
from mobileAC.models import AC

class ACUpdateForm(ModelForm):
    class Meta:
        model = AC
        fields = ('isOn', 'temperature', 'fanSpeed')
        widgets = {'isOn': RadioSelect, 'temperature': TextInput(attrs={'size':'1'}), 'fanSpeed': RadioSelect}
