from rest_framework import serializers
from ledger.models import IncomesCategory, ExpensesCategory, Incomes, Expenses
from users.models import User


class IncomesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomesCategory
        fields = ['id', 'name']

class ExpensesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomesCategory
        fields = ['id', 'name']


class IncomeAddSerializer(serializers.ModelSerializer):
    #
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # category = serializers.PrimaryKeyRelatedField(queryset=IncomesCategory.objects.all())
    # #
    class Meta:
        model = Incomes
        fields = ['user', 'category', 'date', 'amount', 'narration']
