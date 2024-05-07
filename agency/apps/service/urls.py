from django.urls import path
from apps.service.views import service_page, Search

urlpatterns = [
    path('', service_page, name="service"),
    path('search/', Search.as_view(), name="search"),
]