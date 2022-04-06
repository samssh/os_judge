from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from . import views

urlpatterns = [
    path('login/',
         views.MyLoginView.as_view(template_name='registration/login.html'),
         name='login'
         ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/',
         PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
         name='password_change'
         ),
    path('password-change/done/',
         PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html', ),
         name='password_change_done'
         ),
    path('profile/', views.profile, name='profile'),
]
