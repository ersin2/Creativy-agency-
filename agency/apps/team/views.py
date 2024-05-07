from django.shortcuts import render

from apps.home.models import Setting
from apps.team.models import Team

# Create your views here.
def team_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    team = Team.objects.get(pk=id)
    context = {
        'setting':setting,
        'team':team,
    }
    return render(request, 'detail_page/team_detail.html', context)