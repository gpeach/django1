from django.http import HttpResponse


def index(request):
    topic_value = request.GET.get('topic', '')
    return HttpResponse(f"<body>welcome to my {topic_value} home page.</body>")