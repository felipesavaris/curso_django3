from django.db import models


#utilizando TextChoices
class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    conotent = models.TextField()
    #adicionando o textchoices
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    #método para mostrar o titulo quando for selecionado no admin

    def full_name(self):
        return self.title + self.sub_title
        # adicionar o full_name no admin para visualizaçao

    full_name.admin_order_field = 'title'
