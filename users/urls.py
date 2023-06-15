from django.urls import path
from .views import SignUpView, ProfileEditView, DeleteUser

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("edit_profile/", ProfileEditView.as_view(), name="edit_profile"),
    path("delete_user/<int:pk>/", DeleteUser.as_view(), name="delete_user"),
]
