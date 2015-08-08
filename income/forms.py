from django import forms

from income.models.target import IncomeTarget


class IncomeTargetForm(forms.ModelForm):
    class Meta:
        model = IncomeTarget
        exclude = ('user',)
