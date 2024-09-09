from django.shortcuts import render
from django.views.generic import View
from apps.products.models import Banner

# Create your views here.

class HomePageView(View):
    def get(self, request):
        banner = Banner.objects.all()
        context = {
            'banners': banner
        }
        return render(request, 'index-4.html', context)
    
class ShopView(View):
    def get(self, request):
        return render(request, 'shop-grid-left.html', {})
    
class AboutView(View):
    def get(self, request):
        return render(request, 'page-about.html', {})
    
class ContactView(View):
    def get(self, request):
        return render(request, 'page-contact.html', {})