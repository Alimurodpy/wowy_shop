from django.urls import path
from apps.products.views import (
    HomePageView, 
    ShopView, 
    AboutView, 
    ContactView,
    CategoryView,
    ProductView,
    FilterView
)

app_name = 'products'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product'),
    path('filter/', FilterView.as_view(), name='filter'),
]