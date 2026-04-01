from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_issues, name='track_issues'),
]
