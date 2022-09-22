from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList
# Create your views here.

def show_watchlist(req):
    data = MyWatchList.objects.all()
    ctx = {
        'data_mywatchlist': data,
        'nama' : 'Naufal Fikri Hakim',
        'id' : '2106750566'
    }
    return render(req, 'mywatchlist.html', ctx)

def show_xml(req):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
def show_json(req):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
def show_html(req):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('html', data), content_type='application/html')