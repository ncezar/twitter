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
from django.urls import reverse_lazy

# Create your views here.


def hashtag_list(request):
    return render(request, 'twitter/hashtag_list.html', {})

def home_timeline(request):
    auth = tweepy.OAuthHandler("IOBoByzw7sXqXe8zrSBL4Iyvq", "4DEC0VOGuevexfBTfy2bERIX8fRQtX5kGQPZ6Nhz3rxupgrb5c")
    auth.set_access_token("1191824923301482501-Hr3h5O0QtIt7ONdMEvbPMMhRca4iuE", "1uf2tlpLCmQwwkT2zxVWcOtPTExSkm4TyjPvwqSYvR79y")

    api = tweepy.API(auth)

    #public_tweets = api.home_timeline()
    # date_since="2019-12-01"
    search_words = request.GET.get('message')
    #print(search)
    tweets = api.search(search_words, lang="en", rpp=100, result_type="recent", wait_on_rate_limit=True)

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

class CadastroDelete(DeleteView):
    model = Hashtag
    template_name="twitter/hashtag_confirm_delete.html"
    success_url = reverse_lazy('hashtag_list')




class HashtagListView(ListView):
    model = Tweet
    template_name = "twitter/filter_list.html"

    def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        context = super(HashtagListView, self).get_context_data(**kwargs)
        return context
