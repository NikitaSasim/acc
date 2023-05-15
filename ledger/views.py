from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Income, IncomeCategory, ExpensesCategory, Expenses


class HomeView(TemplateView):
    template_name = "base.html"

    def get(self, request):
        incomes = Income.objects.filter(user=request.user)

        params = {
            'incomes': incomes
        }

        return render(request, self.template_name, params)
