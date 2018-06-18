from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from . import views

urlpatterns = [
    url(r'^$', views.hello, name = "hello"),
    url(r'^registration/', views.UserFormView.as_view(), name = "register"),
    url(r'^inventory/', views.inventory, name = "inventory"),
    url(r'^add/', views.add, name = "add"),
    url(r'^addarms/', views.addarms.as_view(), name = "addarms"),
    url(r'^selectupdate/', views.selectupdate, name = "selectupdate"),
    url(r'^/(?P<pk>[0-9]+)/$', views.updatearms.as_view(), name = "updatearms"),
    url(r'^login/', auth_views.login, {'template_name': 'myapp/login.html'},name ="login"),
    url(r'^logout/', auth_views.logout, {'template_name': 'myapp/logout.html', 'next_page': reverse_lazy('hello')}, name = "logout"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]