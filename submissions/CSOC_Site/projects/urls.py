from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('team/<str:team_name>/', views.TeamView.as_view(), name='team')
]