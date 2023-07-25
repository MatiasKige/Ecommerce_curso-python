from django.shortcuts import render
from blog.models import Articles
from django.views.generic import ListView, DetailView

# Create your views here.


class List_articles(ListView):
    model = Articles
    template_name = "articles/list_articles.html"



class Detail_article(DetailView):
    model= Articles
    template_name = "articles/detail_articles.html"
































def create_article(request):
    new_article = Articles.objects.create(
        title="Bajo el peso",
        description="Esta bajisimo, desesperen o salgan a comprar mas!!!",
        author="José Francisco de San Martín")
    context={
        "new_article":new_article
    }
    return render (request,"articles/new_articles.html",context=context)