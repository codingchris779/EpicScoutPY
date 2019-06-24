from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question, Team, Info


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'scout/results.html', {'question': question})


def index(request):
    latest_team_list = Team.objects.order_by('-TeamNum')[:30]
    context = {'latest_team_list': latest_team_list}
    return render(request, 'scout/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'scout/detail.html', {'question': question})


def vote(request):
    info = Info()
    info.Team = get_object_or_404(Team, pk=request.GET["num"])
    if request.GET['side'] == "red":
        info.isRed = True
    else:
        info.isRed = False
    info.MatchNum = 0

