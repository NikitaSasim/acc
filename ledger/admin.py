from django.contrib import admin
from .models import IncomesCategory, Incomes, ExpensesCategory, Expenses


@admin.register(IncomesCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


@admin.register(ExpensesCategory)
class ExpensesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


@admin.register(Incomes)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['date', 'user', 'category', 'amount', 'narration']


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['date', 'user', 'category', 'amount', 'narration']
