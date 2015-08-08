from django import forms


class IncomeRecordForm(forms.ModelForm):
    timestamp = forms.SplitDateTimeField()
    number = forms.DecimalField(min_value=0, decimal_places=2)