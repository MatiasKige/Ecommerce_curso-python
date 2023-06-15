from django.shortcuts import render
from blog.models import Articles

# Create your views here.

def create_article(request):
    new_article = Articles.objects.create(
        title="Bajo el peso",
        description="Esta bajisimo, desesperen o salgan a comprar mas!!!",
        author="José Francisco de San Martín",
    )
    context={
        "new_article":new_article
    }
    return render (request,"articles/new_articles.html",context=context)

"""def list_article(request):
    articles = Articles.objects.all()
    context={
        "articles":articles
    }
    return render(request, "articles_list.html",context=context)"""