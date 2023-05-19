from django import forms
from .models import Incomes, Expenses, IncomesCategory, ExpensesCategory


class IncomesForm(forms.ModelForm):

    class Meta:
        model = Incomes
        fields = ('date', 'category', 'amount', 'narration')


class ExpensesForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = ('date', 'category', 'amount', 'narration')


class IncomesCategoryForm(forms.ModelForm):

    class Meta:
        model = IncomesCategory
        fields = ('name',)


class ExpensesCategoryForm(forms.ModelForm):

    class Meta:
        model = ExpensesCategory
        fields = ('name',)


