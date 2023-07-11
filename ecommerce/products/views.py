from django.shortcuts import render
from products.models import Products
from products.forms import Formulario_productos

def create_product(request):
    if request.method == "POST":
        pass
        # new_product = Products.objects.create(
        #     name="Coca cola",
        #     price=650, stock=10
        #     )
        # context={
        #     "new_product":new_product
        # }
    
    elif request.method =="GET":
        form = Formulario_productos()
        context={
            "form":form
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