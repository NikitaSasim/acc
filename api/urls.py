from django.urls import path
from .views import IncomesCategoriesList, ExpensesCategoryList

urlpatterns = [
    path('incomes_categories/', IncomesCategoriesList.as_view(), name='incomes_categories'),
    path('expenses_categories/', ExpensesCategoryList.as_view(), name='expenses_categories')
]