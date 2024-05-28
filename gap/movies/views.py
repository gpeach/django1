from django.http import HttpResponse

def index(request):
    return HttpResponse("<body>welcome to my movies home page.</body>")