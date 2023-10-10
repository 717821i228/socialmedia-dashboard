from django.urls import path
from . import views

urlpatterns = [
    path('as/',views.index, name='index'),
    path('login/',views.index1, name='index1'),
]