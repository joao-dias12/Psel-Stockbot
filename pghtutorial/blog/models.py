from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model): #subclass da Model o nome é post pois haverão postagens
    title = models.CharField(max_length=255) # Todo post necessita um Título e o maximo serão 255 caracteres
    slug = models.SlugField(max_length=255, unique = True) # é o texto na url dos posts, por exemplo www.meusite.com/blog/ (o que estiver no slug) e ele será unico e não se repete na tabela
    author = models.ForeignKey(User, on_delete=models.CASCADE) #autor do post, o propio User ja vem com varias funções como nome , lastname, email , etc. many to one => um autor pdoe escrever varios posts e se usuário for excluído , os posts são deletados, como é um texto , não tem limite , diferente do titulo
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True) #essa tabela ira adicionar exatamente a hora que foi adicionado o post
    updated = models.DateTimeField(auto_now=True) # nesse caso a cada modificação no artigo, ele irá atualizar automaticamente.
    class Meta:
        ordering = ("-created",)
    def __str__(self): #nome do post retorna ao titulo do mesmo
        return self.title
    def get_absolute_url(self): # fazer link para o url do artigo sozinho no propio blog, apertando no link e chegando ao artigo
        return reverse("blog:detail", kwargs={"slug": self.slug})
    


# Create your models here.
