from django.contrib import admin
from .models import Post


#cria uma melhor visualizaçao dos registros no admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'categories']
    # cria as visualizaões do dados cadastrados

    search_fields = ['title', 'sub_title'] # add item de pesquisa - lupa
    #existe também o filter_horizontal para casos de muitos pra muitos

    #fields = ['title']
    # este caso não apareceria mais o sub_title no admin


admin.site.register(Post, PostAdmin)
#isto add a model ao admin
