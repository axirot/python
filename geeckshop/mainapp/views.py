# Create your views here.

from django.shortcuts import render
import json, os
from mainapp.models import Product, ProductCategory

JSON_PATH = 'mainapp/json'

def loadMenuFromJSON():
    with open(os.path.join(JSON_PATH, 'menu.json'), 'r') as infile:
        return json.load(infile)

def main(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'username' :  'ivan', 'array' : [1, 2, 3, 4, 5]}
    return render(request, 'mainapp/main.html', context)

def products(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)

def contacts(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu}
    return render(request, 'mainapp/contacts.html', {'title': 'Kontakti'})
