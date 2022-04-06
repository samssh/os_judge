from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


def redirect_root(request):
    return redirect('/users/profile/')


urlpatterns = \
    [
        path("admin/", admin.site.urls),
        path("users/", include("account.urls")),
        path("judge/", include("judge.urls")),
        path("", redirect_root, name='root'),
    ]
