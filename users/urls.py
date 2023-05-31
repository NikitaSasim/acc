from django.urls import path
from .views import SignUpView, ProfileEditView, DeleteUser, StripeConfigView
    # StripeCheckoutView, stripe_webhook


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("edit_profile/", ProfileEditView.as_view(), name="edit_profile"),
    path("delete_user/<int:pk>/", DeleteUser.as_view(), name="delete_user"),
    path("config/", StripeConfigView.as_view(), name="stripe-config"),
    # path("create-checkout-session/", StripeCheckoutView.as_view(), name="stripe-create-checkout-session"),
    # path("webhook/", stripe_webhook, name="stripe-webhook")
]
