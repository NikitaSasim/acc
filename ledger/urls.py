from django.contrib import admin
from django.urls import path
from .views import HomeView, CreateIncome, CreateExpense

urlpatterns = [
    path("", HomeView.as_view(), name="ledger-home"),
    path("add_income/", CreateIncome.as_view(), name="add-income"),
    path("add_expense/", CreateExpense.as_view(), name="add-expense")
]
