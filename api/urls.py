from django.urls import path
from .views import IncomesCategoriesListApiView, ExpensesCategoryListApiView,\
    IncomeAddApiView, UserTransactionsApiView, SetIdApiView, ExpenseAddApiView

urlpatterns = [
    path('incomes_categories/', IncomesCategoriesListApiView.as_view(), name='incomes_categories'),
    path('expenses_categories/', ExpensesCategoryListApiView.as_view(), name='expenses_categories'),
    path('user/', UserTransactionsApiView.as_view(), name='user'),
    path('post_income/', IncomeAddApiView.as_view(), name='post_income/'),
    path('post_expense/', ExpenseAddApiView.as_view(), name='post_expense/'),
    path('add_tg/', SetIdApiView.as_view(), name='add_tg')
]
