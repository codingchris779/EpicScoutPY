from django.shortcuts import render
#
# # Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.shortcuts import get_object_or_404, render

from .models import Info, Team, Match, SkystoneMatch
from .forms import InfoForm, MatchForm


def match_data(request,comp, info):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            m = SkystoneMatch()
            i = get_object_or_404(Info, id=info)
            m.info = i
            m.Did_They_Run = bool(form.cleaned_data['Did_They_Run'])
            m.Claiming = bool(form.cleaned_data['Claiming'])
            m.Comments = form.cleaned_data['Comments']
            m.Depot = int(form.cleaned_data['Depot'])
            m.Endgame = form.cleaned_data['Endgame']
            m.Gold_In_Cargo = int(form.cleaned_data['Gold_In_Cargo'])
            m.Silver_In_Cargo = int(form.cleaned_data['Silver_In_Cargo'])
            m.How_Many_Seconds_Were_They_Broke = int(form.cleaned_data['How_Many_Seconds_Were_They_Broke'])
            m.Landing = bool(form.cleaned_data['Landing'])
            m.Park = bool(form.cleaned_data['Park'])
            m.Penalties = int(form.cleaned_data['Penalties'])
            m.Sampling = bool(form.cleaned_data['Sampling'])
            m.save()
            return HttpResponseRedirect('/')
    else:
        form = MatchForm()
    return render(request, 'scout/skystone-form.html', {'form': form, 'competition':comp})


def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            i = Info()
            i.Team = form.cleaned_data['team']
            i.MatchNum = form.cleaned_data['round']
            i.isRed = bool(form.cleaned_data['side'])
            i.save()
            return HttpResponseRedirect('match-data/Newark/'+str(i.id))
    else:
        form = InfoForm()
    return render(request, 'scout/index.html', {'form': form})


def login(request):
    return render(request, 'scout/login.html', {})

def signup(request):
    return render(request, 'scout/new-account.html', {})

def matches_for_view(request):
    matches = SkystoneMatch.objects.all()
    return render(request, 'scout/match-data.html', {'matches': matches})


def clean_matches_for_view(request):
    matches = SkystoneMatch.objects.all()
    return render(request, 'scout/matches.html', {'matches': matches})


