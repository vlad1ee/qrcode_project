from django.urls import path
from .views import index, edo, ofd, mark, SpecificationCreateView


urlpatterns = [
    path('', index, name='index'),
    path('edo/', edo, name='edo'),
    path('ofd/', ofd, name='ofd'),
    path('mark/', mark, name='mark'),
    path('specification/', SpecificationCreateView.as_view(),
         name='specification_create'),
]