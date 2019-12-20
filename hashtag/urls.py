from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.CadastroListView.as_view(), name='hashtag_list'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('delete/<int:pk>', views.CadastroDelete.as_view(), name='cadastro_delete'),
    path('home_timeline', views.home_timeline, name='home_timeline'),
]
