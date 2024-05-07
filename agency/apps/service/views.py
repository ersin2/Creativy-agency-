from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.
from apps.home.models import Setting
from apps.service.models import Service
from apps.portfolio.models import Partners

# Create your views here.

def service_page(request):
    setting = Setting.objects.get(pk=1)
    services = Service.objects.all()
    partners = Partners.objects.all()
    context = {
        'setting':setting,
        'services':services,
        'partners':partners,
    }
    return render(request, 'pages/service.html', context)


class Search(ListView):
    """Поиск Услуги"""
    paginate_by = 3
    template_name = 'search.html'

    def get_queryset(self):
        return Service.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

