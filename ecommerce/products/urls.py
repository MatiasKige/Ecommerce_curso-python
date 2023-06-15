from django.urls import path
from products.views import create_product, list_product

urlpatterns = [
    path("create-product/",create_product,name="create_product"),
    path("list-product/",list_product,name="list_product")
]