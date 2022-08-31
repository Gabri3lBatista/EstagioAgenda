from django.urls import path
from .views import index,adm, login
app_name = 'usuario'

urlpatterns = [
     path('', index),
     path('adm/',adm),
     path('login/',login)
]
