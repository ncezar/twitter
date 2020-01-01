# Twitter Django

O twitter-django é um  projeto destinado para filtrar tweets por usuário, mensagem e data de criação de hashtags criadas.


### Prerequisites

-Python 3.6.2;
-Django;
-Conta developer no twitter para utilizar credenciais;



### Installing

Utilizando Ubuntu 16 e seguindo instruções do Django Girls Tutorial: https://tutorial.djangogirls.org/pt/django/

```
1- Clonar o repositório;
2- Acesse o diretório do seu projeto e execute:
  python3 -m venv myvenv
3- Ative o ambiente através da linha de comando:
  . myvenv/bin/activate
4- Instale os requisitos do projeto:
  pip install -r requirements.txt
5- Para criar o banco de dados:
  python manage.py migrate
6- Crie seu super usuário para ter acesso à guia de administração do seu projeto:
  python manage.py createsuperuser
7- Acesse o arquivo views.py dentro da pasta 'hashtag' e sobrescreva as credenciais do twitter na função 'home_timeline' com as de sua conta em:
  consummer_key
  consummer_secret
  acess_key
  acess_secret
8- Para rodar a aplicação:
  python manage.py runserver
  E então acesse em seu navegador pelo endereço: 127.0.0.1:8000/
9- Experimente em: twitter-django.herokuapp.com/
10- Crie hashtags e clicando em cada umqa delas, você irá acompanhar os tweets mais recentes sobre aquele assunto em inglês

```



## Running the tests

Teste simples para verificar se a criação de uma hashtag foi bem sucedida.


```
python manage.py test
```


## Deployment

```
1- Criar uma conta na Heroku
2- Dentro do diretório do seu projeto, logue na Heroku:
  heroku login
3- Crie um Procfile
4- Atualize o requirements.txt com o gunicorn
5- Crie um app na Heorku para hospedar seu projeto
6- Suba a aplicação através do comando:
  heroku git:remote -a seuapp
  git add .
  git commit -m "Deploy da aplicação"
  git push -u heroku master
7- Acesse o endereço do app da heroku

```
