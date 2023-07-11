from django.shortcuts import render
from products.models import Products

def create_product(request):
    new_product = Products.objects.create(
        name="Coca cola",
          price=650, stock=10
          )
    context={
        "new_product":new_product
    }
    return render (request,"products/new_product.html",context=context)

def list_product(request):
    products = Products.objects.all()
    context={
        "products":products
    }
    return render(request, "products/products_list.html",context=context)

def primer_formulario(request):
    print (request.method)
    if request.method == "POST":
        print (request.POST)
    return render(request, "products/primer_formulario.html", context={})