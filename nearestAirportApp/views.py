from .models import Airportslist
from django.http import HttpResponse
from django.shortcuts import render
import json
from geopy.distance import great_circle


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

    print(nearest_airport)

    icao = nearest_airport[0]
    type = nearest_airport[1]
    name = nearest_airport[2]
    lat = nearest_airport[3]
    lon = nearest_airport[4]
    elevation = nearest_airport[5]
    country = nearest_airport[6]
    region = nearest_airport[7]

    return HttpResponse(json.dumps({'icao': icao,
                                    'type': type,
                                    'name': name,
                                    'lat': lat,
                                    'lon': lon,
                                    'elevation': elevation,
                                    'country': country,
                                    'region': region}), content_type="application/json")


def index(request):
    template = 'nearestAirportApp/index.html'
    return render(request, template)
