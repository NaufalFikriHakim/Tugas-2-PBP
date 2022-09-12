from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(req):
    data_katalog = CatalogItem.objects.all()
    ctx = {
        'list_katalog':  data_katalog,
        'nama': 'Naufal Fikri Hakim',
        'id': '2106750566'

    }

    return render(req, "katalog.html", ctx)