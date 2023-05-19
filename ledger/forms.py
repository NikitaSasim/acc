from django import forms
from .models import Incomes, Expenses


class IncomesForm(forms.ModelForm):

    class Meta:
        model = Incomes
        fields = ('date', 'category', 'amount', 'narration')


