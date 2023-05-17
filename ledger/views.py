from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Income, IncomeCategory, ExpensesCategory, Expenses


class HomeView(TemplateView):
    template_name = "base.html"

    def get(self, request):
        incomes = Income.objects.filter(user=request.user)
        categories = [[k, sum(list(income.amount for income in incomes.filter(category__name=k)))] for k in list(category.name for category in request.user.income_category.all())]

        total = sum([income.amount for income in incomes])

        params = {
            'incomes': incomes,
            'categories': categories,
            'total': total
        }

        return render(request, self.template_name, params)
