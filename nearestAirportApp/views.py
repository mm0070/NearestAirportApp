from .models import Airportslist
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json
from django.core import serializers
from geopy.distance import great_circle

from django.shortcuts import render_to_response
from django.template import RequestContext


def search(request):
    lat = 0
    lon = 0
    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']

    airports_list = Airportslist.objects.all()
    nearest_airport = None

    for entry in airports_list:
        airport = [entry.icao, entry.type, entry.name, entry.lat, entry.lon, entry.elevation, entry.country, entry.region]
        current_airport_lat = airport[3]
        current_airport_lon = airport[4]

        aircraft_location = (lat, lon)
        current_airport_location = (current_airport_lat, current_airport_lon)
        distance = great_circle(aircraft_location, current_airport_location).miles

        airport.append(distance)

        if nearest_airport is None:
            nearest_airport = airport
        elif nearest_airport[8] > distance:
            nearest_airport = airport

    print(lat)
    print(lon)
    lat_lon = "RESPONSE FROM THE SERVER"

    print(nearest_airport)
    return HttpResponse(json.dumps({'lat_lon': lat_lon}), content_type="application/json")


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