from django.shortcuts import render
from apps.home.models import Setting
from apps.portfolio.models import Portfolio
from apps.news.models import News


# Create your views here.

def portfolio_page(request):
    setting = Setting.objects.get(pk=1)
    portfolio = Portfolio.objects.all()
    news = News.objects.all()
    context = {
        'setting':setting,
        'news':news,
        'portfolio':portfolio,
    }
    return render(request, 'pages/portfolio.html', context)