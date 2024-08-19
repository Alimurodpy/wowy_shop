from django.urls import path
from apps.accounts.views import TestView

app_name = 'accounts'

urlpatterns = [
    path('', TestView.as_view(), name='test'),
]


