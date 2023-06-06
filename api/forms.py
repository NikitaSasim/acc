from django import forms
from ledger.models import IncomesCategory, ExpensesCategory, Incomes, Expenses


class IncomeApiForm(forms.ModelForm):
    class Meta:
        model = Incomes
        fields = ['date', 'amount', 'narration']
