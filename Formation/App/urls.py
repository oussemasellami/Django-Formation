from django.urls import path
# from App.views import index
from App.views import *

urlpatterns = [

    path('i/', index),
    path('ii/<str:up>', home),
    path('aff/', affiche, name='AFF'),
    path('affiche/', afficheLV.as_view()),
    path('delete/<int:pk>', Delete.as_view(), name='deletep'),
    path('add/', projetCreateView.as_view(), name='add'),

]
