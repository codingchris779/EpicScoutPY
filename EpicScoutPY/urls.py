from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scout/', include('scout.urls')),
    path('', RedirectView.as_view(url='/scout/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
]
