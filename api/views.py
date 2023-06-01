from rest_framework import generics
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from ledger.models import IncomesCategory, ExpensesCategory, Incomes, Expenses
from users.models import User


class IncomesCategoriesList(generics.ListAPIView):
    serializer_class = serializers.IncomesCategorySerializer
    queryset = IncomesCategory.objects.all()

    def get_queryset(self):

        queryset = IncomesCategory.objects.all()
        user_id = self.request.query_params.get('user')
        queryset = queryset.filter(user__id=user_id)
        return queryset


class ExpensesCategoryList(generics.ListAPIView):
    serializer_class = serializers.IncomesCategorySerializer
    queryset = IncomesCategory.objects.all()

    def get_queryset(self):
        queryset = ExpensesCategory.objects.all()
        user_id = self.request.query_params.get('user')
        queryset = queryset.filter(user__id=user_id)
        return queryset




