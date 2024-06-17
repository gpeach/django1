from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     topic_value = request.GET.get('topic', '')
#     return HttpResponse(f"<body>welcome to my {topic_value} home page.</body>")

def home(request):
    return render(request, 'home.html')