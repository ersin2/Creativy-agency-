from django.shortcuts import render

# Create your views here.
from .models import Setting
from apps.service.models import Service
from apps.team.models import Team, SocialMedia
from apps.news.models import News
from apps.portfolio.models import Portfolio, Partners
from apps.price.models import Price

def home(request):
    setting = Setting.objects.get(pk=1)
    service = Service.objects.all()
    team = Team.objects.all()
    social_media = SocialMedia.objects.all()
    news = News.objects.all()
    portfolio = Portfolio.objects.all()
    partners = Partners.objects.all()
    price = Price.objects.all()
    context = {
        'setting':setting,
        'services':service,
        'teams':team,
        'news':news,
        'portfolios':portfolio,
        'partners':partners,
        'prices':price,
        'social_media':social_media,
    }
    return render(request, 'index.html', context)

def contact_page(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting':setting,
    }
    return render(request, 'pages/contactus.html', context)


def about_page(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting':setting,
    }
    return render(request, 'pages/about.html', context)

def service_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    service = Service.objects.get(pk=id)
    context = {
        'setting':setting,
        'service':service,
    }
    return render(request, 'detail_page/service_detail.html', context)