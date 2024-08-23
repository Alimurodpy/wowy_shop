from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from apps.accounts.form import UserForm

# Create your views here.

class TestView(View):
    def get(self, request):
        return render(request, 'test.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'page-login-register.html', {})
    
    def post(self, request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(username=phone, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('products:home')
        messages.error(request, 'Incorrect phone or password')
        return render(request, 'page-login-register.html', {})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.warning(request, 'Logout successfully')
        return redirect('products:home')
    
class RegisterView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Register successfully')
            return redirect('accounts:login')
        return render(request, 'register.html', {'form': form})