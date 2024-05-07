from django.urls import path
from apps.home.views import home, contact_page,about_page, service_detail
from apps.team.views import team_detail

urlpatterns = [
    path('', home, name="home"),
    path('contact-us/', contact_page, name="contact"),
    path('about-us/', about_page, name="about"),
    path('service/<int:id>/<slug:slug>/', service_detail, name="service_detail"),
    path('team/<int:id>/<slug:slug>/', team_detail, name="team_detail"),
]