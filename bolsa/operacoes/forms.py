from django import forms
from .models import Operacao


class OperacaoForm(forms.ModelForm):
    class Meta:
        model = Operacao
        fields = "__all__"
        