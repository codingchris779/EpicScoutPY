from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.shortcuts import get_object_or_404, render

from .models import Choice, Question
from .forms import InfoForm


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'scout/results.html', {'question': question})


def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/detail/')
    else:
        form = InfoForm()
    return render(request, 'scout/index.html', {'form': form})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'scout/detail.html', {'question': question})

#
# def vote(request):
#     if request.method == 'POST':
#         form = InfoForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/detail/')
#     else:
#         form = InfoForm()
#     return render(request, index.html)
#
#
