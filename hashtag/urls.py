from django.urls import path
from . import views

urlpatterns = [
    path('', views.CadastroListView.as_view(), name='hashtag_list'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('home_timeline', views.home_timeline, name='home_timeline'),
]
