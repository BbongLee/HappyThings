from django import forms

from .models import HappyThings

class HappyThingForm(forms.ModelForm):

    class Meta:
        model = HappyThings
        fields = ('reporter','thing','happinessIndex','effortIndex','desc',)