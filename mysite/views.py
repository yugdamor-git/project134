from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>I am home</h1>")