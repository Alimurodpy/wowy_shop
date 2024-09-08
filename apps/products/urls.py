from django.urls import path
from apps.products.views import HomePageView, ShopView, AboutView, ContactView

app_name = 'products'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]