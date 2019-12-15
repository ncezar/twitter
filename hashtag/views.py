from django.shortcuts import render
from .forms import CadastroForm
from .forms import Hashtag
from .models import Tweet
from django.contrib import messages
from django.utils import timezone
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.


def hashtag_list(request):
    return render(request, 'twitter/hashtag_list.html', {})

def posts(request):
    return render(request, 'twitter/filter_list.html', {})

def cadastro(request): #CadastroCreate
    if request.method=='POST':
        form = CadastroForm(request.POST or None)
        if form.is_valid():
            messages.success(request, 'Enviado com sucesso!')
            form.save()
    else:
        form = CadastroForm()
    context = {'form': form}
    return render(request, "twitter/cadastro.html", context)


class CadastroListView(ListView):
    model = Hashtag
    template_name = "twitter/hashtag_list.html"


    def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        context = super(CadastroListView, self).get_context_data(**kwargs)
        return context

class HashtagListView(ListView):
    model = Tweet
    template_name = "twitter/filter_list.html"


    def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        context = super(HashtagListView, self).get_context_data(**kwargs)
        return context
