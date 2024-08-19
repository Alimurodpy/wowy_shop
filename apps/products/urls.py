from django.urls import path
from apps.products.views import HomePageView

app_name = 'products'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]