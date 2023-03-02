from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.UserRegisterView.as_view(), name="registration"),
    path('logout/', views.logout_student, name="logout")


]