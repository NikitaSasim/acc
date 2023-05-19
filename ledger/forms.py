from django import forms
from .models import Incomes, Expenses


class IncomesForm(forms.ModelForm):

    class Meta:
        model = Incomes
        fields = ('date', 'category', 'amount', 'narration')


class ExpensesForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = ('date', 'category', 'amount', 'narration')


