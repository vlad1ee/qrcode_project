from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('edo/', edo, name='edo'),
    path('ofd/', ofd, name='ofd'),
    path('mark/', mark, name='mark'),
]