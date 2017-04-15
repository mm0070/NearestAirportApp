from .models import Airportslist
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json
from django.core import serializers

def index(request):
    first_50_airports = Airportslist.objects.all()[:50]
    context = {'first_50_airports': first_50_airports}
    return render(request, 'nearestAirportApp/index.html', context)

def detail(request, icao):
    first_50_airports = Airportslist.objects.filter(name=icao)
    template = loader.get_template('nearestAirportApp/index.html')
    print(first_50_airports[0].lat - 10)
    context = {
        'first_50_airports': first_50_airports,
    }
    return HttpResponse(template.render(context, request))

# def detail(request, icao):
#     return HttpResponse("You're looking at airport: %s." % icao)


def tasks_json(request):
    tasks = Task.objects.all()
    data = serializers.serialize("json", tasks)
    return HttpResponse(data, content_type='application/json')