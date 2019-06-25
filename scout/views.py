from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.shortcuts import get_object_or_404, render

from .models import Choice, Question, Info, Team
from .forms import InfoForm


def match_data(request, info):
    return HttpResponse(str(info))


def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            i = Info()
            i.Team = get_object_or_404(Team, id=form.cleaned_data['team'])
            i.MatchNum = form.cleaned_data['round']
            i.isRed = bool(form.cleaned_data['side'])
            i.save()
            return HttpResponseRedirect('match-data/'+str(i.id))
    else:
        form = InfoForm()
    return render(request, 'scout/index.html', {'form': form})

