from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm, ProfileEditForm

import re
from .models import User
from django.urls import reverse_lazy
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# import stripe


class SignUpView(TemplateView):
    template_name = "registration/registration.html"

    def get(self, request):

        return render(request, self.template_name, )

    def post(self, request):
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            user_form.save_m2m()

            new_user = authenticate(
                email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password2']
            )

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




class StripeConfigView(View):
    def get(self, request):
        stripe_config = {"publicKey": settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


# class StripeCheckoutView(View):
#     def get(self, request):
#         domain_url = "http://localhost:8000"
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         try:
#             user_id = request.user.id  # Get the user ID
#             url = f"{domain_url}{request.user.get_user_url()}"
#             print(url)
#             checkout_session = stripe.checkout.Session.create(
#                 success_url=f"{domain_url}{request.user.get_user_url()}",
#                 cancel_url=domain_url,
#                 mode='payment',
#                 line_items=[
#                     {
#                         "price": "price_1N1Y8aDwbEIL0c1OlNOZ3mpi",
#                         "quantity": 1,
#                     },
#                 ],
#                 metadata={  # Include the user ID in the metadata
#                     'user_id': user_id
#                 }
#             )
#             print(checkout_session)
#             return JsonResponse({'sessionId': checkout_session['id']})
#         except Exception as e:
#             return JsonResponse({"error": str(e)})
#
#
# @csrf_exempt
# def stripe_webhook(request):
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None
#
#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, endpoint_secret)
#     except ValueError as e:
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         return HttpResponse(status=400)
#
#     if event['type'] == 'checkout.session.completed':
#         print("Payment was successful!")
#         session = event['data']['object']
#         user_id = session['metadata']['user_id']  # Retrieve the user ID from the metadata
#         user = User.objects.get(id=user_id)
#         user.is_verified = True
#         user.save()
#     return HttpResponse(status=200)
