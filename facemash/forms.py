from django import forms
from .models import Image

class Vote_image(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        
