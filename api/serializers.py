from rest_framework import serializers
from ledger.models import IncomesCategory, ExpensesCategory


class IncomesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomesCategory
        fields = ['id', 'name']


class ExpensesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesCategory
        fields = ['id', 'name']



