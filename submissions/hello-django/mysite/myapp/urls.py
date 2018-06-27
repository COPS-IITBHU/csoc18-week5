from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
app_name = 'myapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),



    # imp https://www.youtube.com/watch?v=mWofrhTwGWQ&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK&index=12
    url(r'^products', views.products, name='products'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.Productdetail.as_view(), name='productdetail'),
    url(r'addproduct/$',views.ProductCreate.as_view(),name='product-add'),

    url(r'^deleteproducts/$', views.deleteproducts, name='deleteproducts'),

    url(r'^product/(?P<pk>[0-9]+)/delete/$', views.ProducDelete.as_view(), name='product-delete'),


]
