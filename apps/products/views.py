from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'index-4.html', {})
    
class ShopView(View):
    def get(self, request):
        return render(request, 'shop-grid-left.html', {})
    
class AboutView(View):
    def get(self, request):
        return render(request, 'page-about.html', {})
    
class ContactView(View):
    def get(self, request):
        return render(request, 'page-contact.html', {})