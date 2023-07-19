from django.urls import path
from products.views import create_product, list_product, primer_formulario, search_products

urlpatterns = [
    path("create-product/",create_product,name="create_product"),
    path("list-product/",list_product,name="list_product"),
    path("primer-formulario/", primer_formulario, name="primer_formulario"),
    path("search-products/", search_products, name="search_products")
]