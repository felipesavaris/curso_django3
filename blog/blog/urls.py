from django.contrib import admin
from django.urls import path
from .views import hello_world
# deve importar toda view criada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
]
