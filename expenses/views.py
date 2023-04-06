from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ExampleForm
from .models import Expense


# Create your views here.
def example(request):
    return render(request,'expenses/example.html')

def home(request):
    return render(request,'expenses/home.html')

def new_data(request):
    return render(request,'expenses/new_data.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in here.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'expenses/register.html', {'form':form})

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ['date', 'expense_type', 'amount', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)