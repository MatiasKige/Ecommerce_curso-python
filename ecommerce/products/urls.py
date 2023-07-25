from django.urls import path
from products.views import create_product, list_product, primer_formulario, search_products, \
    delete_prudct, update_product

urlpatterns = [
    path("create-product/",create_product,name="create_product"),
    path("list-product/",list_product,name="list_product"),
    path("primer-formulario/", primer_formulario, name="primer_formulario"),
    path("search-products/", search_products, name="search_product"),
    path("delete-product/<int:pk>/",delete_prudct, name="delete_product"),
    path("update-product/<int:pk>/",update_product,name="update_product")
]