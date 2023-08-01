from django.contrib import admin
from django.urls import path, include
from ecommerce.views import segundo_template, template_con_lista, template_notas, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("segundo-template/",segundo_template,name="segundo_template"),
    path("template-con-lista/",template_con_lista,name="template_con_lista"),
    path("template-notas/", template_notas, name="template_notas"),
    path("products/",include("products.urls")),
    path("articles/",include("blog.urls")),
    path("users/",include("users.urls"))
]
