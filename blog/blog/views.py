from django.http import HttpResponse


def hello_world(request):
#por padrão toda view recebe request
    return HttpResponse('Hello World!')
