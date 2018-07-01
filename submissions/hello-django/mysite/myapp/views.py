from django.http import HttpResponse

def hello(request):
    return HttpResponse("<p>Hello, world</p>")
