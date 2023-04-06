"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from expenses import views as expenses_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", expenses_views.home, name='home'),
    path("new-data", expenses_views.new_data, name='new-data'),
    path("login/", auth_views.LoginView.as_view(template_name='expenses/login.html'), name='login'),
    path("register/", expenses_views.register, name='register'),
    path("logout/", auth_views.LogoutView.as_view(template_name='expenses/logout.html'), name='logout'),
    path("expense/new/", expenses_views.ExpenseCreateView.as_view(), name='expense-create'),
    path("example/", expenses_views.example, name='example'),
]  