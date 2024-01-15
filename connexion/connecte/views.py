from django.shortcuts import render, get_object_or_404
from .models import produit
from django.http import HttpResponse


def index (request):
    produits=produit.objects.all()
    return render(request, template_name='connecte/index.html', context={'produits':produits})

def produit_detail(request,slug):
    un_produit= get_object_or_404(produit,slug=slug)
    return render(request, template_name='connecte/produit.html', context={'un_produit': un_produit})