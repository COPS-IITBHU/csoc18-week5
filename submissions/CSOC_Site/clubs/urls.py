from django.urls import path
from clubs import views

app_name = 'clubs'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
]