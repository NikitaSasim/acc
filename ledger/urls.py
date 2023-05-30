from django.contrib import admin
from django.urls import path
from .views import HomeView, CreateIncome, CreateExpense, AddCategoryExpenses, \
    AddCategoryIncomes, DeleteIncomesCategoryView, DeleteExpensesCategoryView, EditIncomesCategoryView, \
    DeleteIncomeView, EditIncomeView, EditExpensesCategoryView, DeleteExpenseView, EditExpenseView

urlpatterns = [
    path("", HomeView.as_view(), name="ledger-home"),
    path("add_income/", CreateIncome.as_view(), name="add-income"),
    path("add_expense/", CreateExpense.as_view(), name="add-expense"),
    path("add_incomes_category/", AddCategoryIncomes.as_view(), name="add-incomes-category"),
    path("add_expenses_category/", AddCategoryExpenses.as_view(), name="add-expenses-category"),
    path("delete_incomes_category/", DeleteIncomesCategoryView.as_view(), name="delete-incomes-category"),
    path("edit_incomes_category/", EditIncomesCategoryView.as_view(), name="edit-incomes-category"),
    path("delete_income/", DeleteIncomeView.as_view(), name="delete-income"),
    path("edit_income/", EditIncomeView.as_view(), name="edit-income"),
    path("delete_expenses_category/", DeleteExpensesCategoryView.as_view(), name="delete-expenses-category"),
    path("edit_expenses_category/", EditExpensesCategoryView.as_view(), name="edit-expenses-category"),
    path("delete_expense/", DeleteExpenseView.as_view(), name="delete-expense"),
    path("edit_expense/", EditExpenseView.as_view(), name="edit-expense"),

]
