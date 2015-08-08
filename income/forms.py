from django import forms

from income.models.target import IncomeTarget


class IncomeRecordForm(forms.ModelForm):
    timestamp = forms.SplitDateTimeField()
    number = forms.DecimalField(min_value=0, decimal_places=2)


class IncomeTargetForm(forms.ModelForm):
    class Meta:
        model = IncomeTarget
        exclude = ('user',)
