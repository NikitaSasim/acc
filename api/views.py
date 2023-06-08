import os

import requests
from rest_framework import generics, status
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from . import serializers
from ledger.models import IncomesCategory, ExpensesCategory, Incomes, Expenses
from users.models import User
import datetime
import json




class IncomesCategoriesListApiView(generics.ListAPIView):
    serializer_class = serializers.IncomesCategorySerializer
    queryset = IncomesCategory.objects.all()

    def get_queryset(self):

        queryset = IncomesCategory.objects.all()
        telegram_id = self.request.query_params.get('user')
        queryset = queryset.filter(user__telegram_id=telegram_id)
        return queryset


class ExpensesCategoryListApiView(generics.ListAPIView):
    serializer_class = serializers.ExpensesCategorySerializer
    queryset = ExpensesCategory.objects.all()

    def get_queryset(self):
        queryset = ExpensesCategory.objects.all()
        telegram_id = self.request.query_params.get('user')
        queryset = queryset.filter(user__telegram_id=telegram_id)
        return queryset


class UserTransactionsApiView(APIView):
    def get(self, request):

        if self.request.query_params.get('token') != os.getenv("TG_TOKEN"):
            print(self.request.query_params.get('token'))
            print(os.getenv("TG_TOKEN"))
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

        telegram_id = self.request.query_params.get('user')
        user = User.objects.get(telegram_id=telegram_id)
        incomes = Incomes.objects.all()
        incomes = incomes.filter(user=user)
        expenses = Expenses.objects.all()
        expenses = expenses.filter(user=user)

        response = {'user': user.id}
        response['currency'] = user.currency

        incomes_list = []
        for item in incomes:
            item_dict = {
                'category': item.category.name,
                'date': item.date.strftime("%d.%m.%Y"),
                'amount': float(item.amount),
                'narration': item.narration
            }
            incomes_list.append(item_dict)

        expenses_list = []
        for item in expenses:
            item_dict = {
                'category': item.category.name,
                'date': item.date.strftime("%d.%m.%Y"),
                'amount': float(item.amount),
                'narration': item.narration
            }
            expenses_list.append(item_dict)

        response['incomes'] = incomes_list
        response['expenses'] = expenses_list

        return Response(response, status=status.HTTP_200_OK)



class IncomeAddApiView(APIView):


    def post(self, request):

        data = request.data.dict()
        print(data)
        try:

            user = User.objects.get(id=int(data['user']))
            print(user)
            category = IncomesCategory.objects.get(id=int(data['category']))
            print(category)
            date = datetime.datetime.strptime(data['date'], '%Y.%m.%d').date()
            print(date)
            amount = float(data['amount'])
            print(amount)
            narration = data['narration']
            print(narration)
            new_income = Incomes(user=user, category=category, date=date, amount=amount, narration=narration)

            new_income.save()
            return Response('Income created', status=status.HTTP_201_CREATED)
        except:
            return Response('Bad data', status=status.HTTP_400_BAD_REQUEST)


class ExpenseAddApiView(APIView):


    def post(self, request):

        data = request.data.dict()
        print(data)
        try:

            user = User.objects.get(id=int(data['user']))
            print(user)
            category = ExpensesCategory.objects.get(id=int(data['category']))
            print(category)
            date = datetime.datetime.strptime(data['date'], '%Y.%m.%d').date()
            print(date)
            amount = float(data['amount'])
            print(amount)
            narration = data['narration']
            print(narration)
            new_expense = Expenses(user=user, category=category, date=date, amount=amount, narration=narration)

            new_expense.save()
            return Response('Expense created', status=status.HTTP_201_CREATED)
        except:
            return Response('Bad data', status=status.HTTP_400_BAD_REQUEST)


class SetIdApiView(APIView):
    def post(self, request):

        data = request.data.dict()
        if data['token'] != os.getenv("TG_TOKEN"):
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = User.objects.get(key=data['key'])
            user.telegram_id = int(data['user'])
            user.key = ''
            user.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response('Bad data', status=status.HTTP_400_BAD_REQUEST)





