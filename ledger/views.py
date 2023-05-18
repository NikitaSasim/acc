from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Incomes, IncomesCategory, ExpensesCategory, Expenses


class HomeView(TemplateView):
    template_name = "base.html"

    def get(self, request):
        incomes = Incomes.objects.filter(user=request.user).order_by('date')
        incomes_categories = [[k, sum(list(income.amount for income in incomes.filter(category__name=k)))]
                      for k in list(category.name for category in request.user.incomes_category.all())]

        incomes_total = sum([income.amount for income in incomes])

        expenses = Expenses.objects.filter(user=request.user).order_by('date')
        expenses_categories = [[k, sum(list(expense.amount for expense in expenses.filter(category__name=k)))]
                             for k in list(category.name for category in request.user.expenses_category.all())]

        expenses_total = sum([expenses.amount for expenses in expenses])


        params = {
            'incomes': incomes,
            'incomes_categories': incomes_categories,
            'incomes_total': incomes_total,
            'expenses': expenses,
            'expenses_categories': expenses_categories,
            'expenses_total': expenses_total
        }

        return render(request, self.template_name, params)
