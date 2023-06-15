from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ledger.urls")),
    path("", include("users.urls")),
    path("", include('allauth.urls')),
    path("api/", include('api.urls')),
    path("accounts/", include("django.contrib.auth.urls"))

]
