from django.shortcuts import render
from django.views.generic import View
from apps.products.models import (
    Banner,
    Service,
    Category,
    Brand
)

# Create your views here.

class HomePageView(View):
    def get(self, request):
        banner = Banner.objects.all()
        service = Service.objects.filter(is_active=True)
        category = Category.objects.all()
        grandparents = Category.objects.filter(parent__isnull=True)
        grandparents_count = grandparents.count()
        children = Category.objects.filter(parent__parent__isnull=False)
        parents_and_children = Category.objects.filter(parent__isnull=False)
        brand = Brand.objects.all().order_by('-created_at')

        # print("grandparents",grandparents, '\n')
        # print("parents",parents_and_children, '\n')
        # print("children",children, '\n')


        context = {
            'banners': banner,
            'services': service,
            'categories': category,
            'grandparents': grandparents,
            'grandparents_count': grandparents_count,
            'children': children,
            'brands': brand

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