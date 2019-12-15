from django import forms
from .models import Hashtag


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['message']
