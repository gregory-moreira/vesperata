from django.urls import path

from . import views
from . import apis

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('event/', apis.ListEventAPI.as_view(), name='evento')
]