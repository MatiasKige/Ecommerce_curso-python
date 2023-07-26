from django.urls import path
from blog.views import create_article, List_articles, Detail_article, Create_article, Delete_article

urlpatterns = [
    # path("create-article/",create_article,name="create_article"),
    path("list-articles/",List_articles.as_view(),name="List_articles"),
    path("detail-article/<int:pk>/",Detail_article.as_view(),name="Detail_article"),
    path("create-article/",Create_article.as_view(),name="Create_article"),
    path("delete-articles/<int:pk>/",Delete_article.as_view(),name="Delete_articles")
]