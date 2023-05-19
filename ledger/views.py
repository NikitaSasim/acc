from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Incomes, IncomesCategory, ExpensesCategory, Expenses
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import IncomesForm, ExpensesForm


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


class CreateIncome(View):

    @method_decorator(login_required)
    def post(self, request):
        if request.method == 'POST':
            form = IncomesForm(request.POST)

            if form.is_valid():

                new_income = form.save(commit=False)
                new_income.user = request.user
                new_income.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                form = IncomesForm()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CreateExpense(View):

    @method_decorator(login_required)
    def post(self, request):
        if request.method == 'POST':
            form = ExpensesForm(request.POST)

            if form.is_valid():

                new_expense = form.save(commit=False)
                new_expense.user = request.user
                new_expense.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                form = ExpensesForm()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
