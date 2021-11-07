# AuthViews
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class AuthLoginView(LoginView):
    template_name = 'auth/login.html'


class AuthLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'auth/logout.html'
