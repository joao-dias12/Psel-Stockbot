from django.urls import path

from . import views

app_name = "blog" #referenciar as urls

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
] #lista de padrões de url: 1 - url sem argumentos , ouseja se a gente coloca a url sem argumentos a gente sai na lista de posts 2: com argumento - logo a gente vai diretamente para url do post daquele argumento específico
