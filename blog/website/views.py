from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post


def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git', 'Htnl', 'Banco de Dados', 'Linux', 'Nginx',
        'Uwsgi', 'Systemctl'
    ]
    list_posts = Post.objects.filter(approved=True)  # ou Post.objects.all()

    data = {
        'name': 'Curso Django 3',
        'lista_tecnologias': lista,
        'posts': list_posts
    }

    return render(request, 'index.html', data)
# o render carrega um template, diferente do httpreponse que estava estático
