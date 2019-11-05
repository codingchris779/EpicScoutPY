"""EpicScoutPY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views


app_name = "scout"
urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /match-data/Newark/5/
    path('match-data/<str:comp>/<int:info>/', views.match_data, name='match_data'),
    path('matches/', views.matches_for_view, name='matches'),
    path('clean-matches/', views.clean_matches_for_view, name='clean_matches'),
    path('skystone-form.html/', views.SkystoneMatch, name='scout_match'),

]
