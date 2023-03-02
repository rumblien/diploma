from django.shortcuts import render, redirect

from django.views.generic import FormView, CreateView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.

from apps.accounts.forms import LoginForm, UserRegisterForm
from apps.accounts.models import User


class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def form_valid(self, form):
        data = form.cleaned_data
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("courses_list")
            return HttpResponse("Вам необходимо актировать аккаунт")
        return HttpResponse("Проверьте введённые вами данные ещё раз!")



def logout_student(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("courses_list")




class UserRegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    model = User
    success_url = reverse_lazy('courses_list')

    def form_valid(self, form):
        user = form.save(commit=True)
        user.is_active = True
        user.save()
        return super().form_valid(form)

