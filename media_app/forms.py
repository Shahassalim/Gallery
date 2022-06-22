from django import forms
from .models import ImgModel

class Imgform(forms.ModelForm):
    class Meta:
        model=ImgModel
        fields='__all__'
