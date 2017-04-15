from .models import Airportslist
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json
from django.core import serializers

from django.shortcuts import render_to_response
from django.template import RequestContext


def search(request):
    lat = 0
    lon = 0
    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']

    print(lat)
    print(lon)
    lat_lon = "RESPONSE FROM THE SERVER"

    return HttpResponse(json.dumps({'lat_lon': lat_lon}), content_type="application/json")
    # return HttpResponse(data, content_type='application/json')
    # return HttpResponse('')
    # return HttpResponse(zipcodes[0].mpoly.geojson, mimetype="application/json")


def index(request):
    template = 'nearestAirportApp/index.html'
    return render(request, template)

# def index(request):
#      first_50_airports = Airportslist.objects.all()[:50]
#      context = {'first_50_airports': first_50_airports}
#      return render(request, 'nearestAirportApp/index.html', context)


# def detail(request, icao):
#     first_50_airports = Airportslist.objects.all()[:50]
#     template = loader.get_template('nearestAirportApp/index.html')
#     print(first_50_airports[0].lat - 10)
#     context = {
#         'first_50_airports': first_50_airports,
#     }
#     return HttpResponse(template.render(context, request))
#
# # def detail(request, icao):
# #     return HttpResponse("You're looking at airport: %s." % icao)
#
#
# def tasks_json(request):
#     tasks = Task.objects.all()
#     data = serializers.serialize("json", tasks)
#     return HttpResponse(data, content_type='application/json')