from django.contrib import admin
from .models import IncomeCategory, Income, ExpensesCategory, Expenses


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


@admin.register(ExpensesCategory)
class ExpensesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['date', 'user', 'category', 'amount', 'narration']


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['date', 'user', 'category', 'amount', 'narration']
