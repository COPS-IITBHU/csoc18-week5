from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Product
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'myapp/index.html')

def products(request):
    all_products = Product.objects.all()
    context = {
    'all_products': all_products,
    }
    return render(request, 'myapp/products.html', context)



class Productdetail(generic.DetailView):
    model = Product
    template_name = 'myapp/productdetails.html'
    context_object_name = 'name'

    def get_queryset(self):
        return Product.objects.all()
#def productdetail(request, product_id):
#    product = Product.objects.get(pk=product_id)
#    data = {'name': product }
#    return render(request, 'myapp/productdetails.html', data)

    # return HttpResponse("<h2>details about product no." + str(product_id) + "</h2>")

class ProductCreate(CreateView):
    model = Product
    fields = ['name','price','description','image']
    template_name = 'myapp/createform.html'


def deleteproducts(request):
    all_products = Product.objects.all()
    context = {
    'all_products': all_products,
    }
    return render(request, 'myapp/productdelete.html', context)

class ProducDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:deleteproducts')

#-----------------
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
