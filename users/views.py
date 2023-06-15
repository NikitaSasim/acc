from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm, ProfileEditForm

from .models import User
from django.urls import reverse_lazy
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
import string
import secrets


from ledger.models import ExpensesCategory, IncomesCategory
from .apps import send_message





class SignUpView(TemplateView):
    template_name = "registration/registration.html"

    def get(self, request):

        return render(request, self.template_name, )

    def post(self, request):
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            alphabet = string.ascii_letters + string.digits
            key = ''.join(secrets.choice(alphabet) for i in range(14))
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.key = key
            new_user.save()

            new_user = authenticate(
                email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password2']
            )
            login(request, new_user)

            incomes_categories = ['Salary',
                                  'Social welfare',
                                  'Property income',
                                  'Other income'
                                  ]

            for category in incomes_categories:
                incomes_category = IncomesCategory.objects.create(name=category, user=new_user)
                incomes_category.save()




            expenses_categories = ['Food',
                                   'Utilities',
                                   'Clothes',
                                   'Recreation and Entertainment',
                                   'Healthcare',
                                   'Car costs',
                                   'Savings and Investments',
                                   'Loan Payments',
                                   'Other expenses'
                                   ]

            for category in expenses_categories:
                expenses_category = ExpensesCategory.objects.create(name=category, user=new_user)
                expenses_category.save()

            send_message(key=key, email=new_user.email)


            return redirect("ledger-home")

        return render(request, self.template_name, {'user_form': user_form,})


class ProfileEditView(TemplateView):
    template_name = "registration/edit_profile.html"

    def get(self, request):
        if request.user.is_authenticated:

            return render(request, self.template_name)
        else:
            return redirect("ledger-home")

    def post(self, request):
        if request.user.is_authenticated:
            user_form = ProfileEditForm(
                request.POST, request.FILES, instance=request.user)

            if user_form.is_valid():
                edit_user = user_form.save()
                edit_user.save()

                return redirect("ledger-home")

            return render(request, self.template_name)
        else:
            return redirect("ledger-home")


class DeleteUser(SuccessMessageMixin, DeleteView):
    model = User
    template_name = "registration/delete_user_confirm.html"
    success_message = "User has been deleted"
    success_url = reverse_lazy("ledger-home")







