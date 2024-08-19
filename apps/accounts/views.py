from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

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
    
class SignupView(View):
    def get(self, request):
        return render(request, 'page-login-signup.html', {})