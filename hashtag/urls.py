from django.urls import path
from . import views

urlpatterns = [
    path('', views.CadastroListView.as_view(), name='hashtag_list'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('posts', views.HashtagListView.as_view(), name='posts'),
]
