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
import tweepy

# Create your views here.


def hashtag_list(request):
    return render(request, 'twitter/hashtag_list.html', {})

def home_timeline(request):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    #public_tweets = api.home_timeline()
    #date_since="2019-12-01"
    search_words = "#prom"
    tweets = api.search(search_words, lang="en", rpp=20)

    return render(request, 'twitter/public_tweets.html', {'public_tweets': tweets})

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
