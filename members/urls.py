from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('', views.index, name='index'),
    path('regform/', views.regform, name='regform'),
    path('about/', views.about, name='about'),
]