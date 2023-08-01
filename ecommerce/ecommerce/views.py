from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    return HttpResponse("Holis, segunda clase con Django")

def segundo_template(request):
    today = datetime.today()
    context = {
        "name":"Matias",
        "last_name":"Gigena",
        "today":today
    }
    return render (request, "template_2.html", context=context)

def template_con_lista(request):
    context = {
        "lista":["tomate", "banana", "naranja"],
    }
    return render (request, "template_lista.html", context=context)

def template_notas(request):
    context = {
        "notas":[7,9,5,3,8]
    }
    return render(request,"template_notas.html",context=context)

def index(request):
    return render(request,"index.html")