from django.shortcuts import render
from django.views.generic import View
from apps.products.models import (
    Banner,
    Service,
    Category,
    Brand,
    Product,
    ProductImage,
    ProductSize,
    AdditionalInfo,
    Review,
    Advertising,
    LimitedTimeOffers
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
        brand = Brand.objects.all().order_by('-created_at')
        popular_products = Product.objects.filter(is_popular=True)
        new_arrival = Product.objects.all().order_by('-created_at')
        advertising = Advertising.objects.all()
        monthly_best_sell = Product.objects.all().order_by('-view_count')
        limited_time_offers = LimitedTimeOffers.objects.all()


        # print("\nadvertising", advertising, '\n')
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
            'brands': brand,
            'popular_products': popular_products,
            'new_arrivals': new_arrival,
            'monthly_best_sell': monthly_best_sell,
            'advertisings': advertising,
            'limited_time_offers': limited_time_offers 

        }
        return render(request, 'index-4.html', context)
    
class ShopView(View):
    def get(self, request):
        product = Product.objects.all()
        
        context = {
            'products': product
        }
        return render(request, 'shop-grid-left.html', context)

class CategoryView(View):
    def get(self, request, slug):
        product = Product.objects.filter(category__slug=slug)
        print("product",product, "#####################################")
        context = {
            'products': product
        }
        return render(request, 'shop-grid-left.html', context)

class AboutView(View):
    def get(self, request):
        return render(request, 'page-about.html', {})
    
class ContactView(View):
    def get(self, request):
        return render(request, 'page-contact.html', {})
    
class ProductView(View):
    def get(self, request, slug): 
        size = request.GET.get('size', None)
        color = request.GET.get('color', None)
    

        if color is None:
            product = ProductSize.objects.filter(product__slug=slug)[0]
            order_image = ProductImage.objects.filter(product__slug=slug)
        elif size is None:
            product = ProductSize.objects.filter(product__slug=slug, color__name=color)[0]
            order_image = ProductImage.objects.filter(product__slug=slug, color__name=color)
        else:
            product = ProductSize.objects.get(product__slug=slug, size__name=size, color__name=color)
            order_image = ProductImage.objects.filter(product__slug=slug, color__name=color)
            
        # if color is None:
        #     order_image = ProductImage.objects.filter(product__slug=slug)
        # else:    
        #     order_image = ProductImage.objects.filter(product__slug=slug, color__name=color)
        
        unique_colors = ProductSize.objects.filter(product__slug=slug).values_list('color__name', flat=True).distinct()
        if color is None:
            unique_sizes = ProductSize.objects.filter(product__slug=slug).values_list('size__name', flat=True).distinct()
        else:
            unique_sizes = ProductSize.objects.filter(product__slug=slug, color__name=color).values_list('size__name', flat=True).distinct()
        

        product.product.view_count += 1
        product.product.save()

        new_price = product.price - ((product.price * product.product.discount) / 100)

        # print('\n',"product.product.view_count ->",product.product.view_count,'\n')
        # print('\n',"product ->",product,'\n')
        # print('\n',"order_product ->",order_product.SKU,'\n')

        # for order_product in order_product:
        #     print('\n',"order_product ->",order_product.size,'\n')
        
        context = {
            'product': product,
            'size' : size,
            'color' : color,
            'unique_colors': unique_colors,
            'unique_sizes': unique_sizes,
            'order_image': order_image,
            'new_price': new_price
        }
        return render(request, 'shop-product-right.html', context)
    
class FilterView(View):
    def post(self, request):
        keywords = request.POST.get('keywords')
        status = request.POST.get('status')
        address= request.POST.get('address')
        bedrooms = request.POST.get('bedrooms')
        garages = request.POST.get('garages')
        bathrooms = request.POST.get('bathrooms')
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')

        filters = Q()
        if keywords:
            filters &= Q(name__icontains=keywords) 
        if status:
            filters &= Q(status__icontains=status)
        if address:
            filters &= Q(address__icontains=address)
        if bedrooms:
            filters &= Q(bed__gte=bedrooms)
        if garages:
            filters &= Q(garage__gte=garages)
        if bathrooms:
            filters &= Q(bath__gte=bathrooms)
        if min_price:
            filters &= Q(price__gte=min_price)
        if max_price:
            filters &= Q(price__lte=max_price)


        properties = House.objects.filter(filters)
        
        context = {
            'properties': properties
        }
        return render(request, 'property-grid.html', context)
    
    def get(self, request, *args, **kwargs):
        return redirect('/')