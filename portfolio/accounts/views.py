from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = '/'
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, "You have been successfully logged out.")
        return redirect(self.next_page)