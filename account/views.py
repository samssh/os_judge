from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'title': _('Profile'), 'pretitle': _('Manage your profile')})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    next_page = "/users/profile/"
    pass
