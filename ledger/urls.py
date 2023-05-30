from django.contrib import admin
from django.urls import path
from .views import HomeView, CreateIncome, CreateExpense, AddCategoryExpenses, \
    AddCategoryIncomes, DeleteIncomesCategoryView, DeleteExpensesCategoryView, EditIncomesCategoryView

urlpatterns = [
    path("", HomeView.as_view(), name="ledger-home"),
    path("add_income/", CreateIncome.as_view(), name="add-income"),
    path("add_expense/", CreateExpense.as_view(), name="add-expense"),
    path("add_incomes_category/", AddCategoryIncomes.as_view(), name="add-incomes-category"),
    path("add_expenses_category/", AddCategoryExpenses.as_view(), name="add-expenses-category"),
    path("delete_incomes_category/", DeleteIncomesCategoryView.as_view(), name="delete-incomes-category"),
    path("expenses/delete_category-<int:id>/", DeleteExpensesCategoryView.as_view(), name="delete-expenses-category"),
    path("edit_incomes_category/", EditIncomesCategoryView.as_view(), name="edit-incomes-category"),

]
