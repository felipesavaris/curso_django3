from django.shortcuts import render
#from django.http import HttpResponse


def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git', 'Htnl', 'Banco de Dados', 'Linux', 'Nginx',
        'Uwsgi', 'Systemctl'
    ]
    data = {'name': 'Curso Django 3', 'lista_tecnologias': lista}
    return render(request, 'index.html', data)
# o render carrega um template, diferente do httpreponse que estava estático
