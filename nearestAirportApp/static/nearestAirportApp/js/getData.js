$(document).on('submit', '#search', function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url:'/nearestAirportApp/search/',
        data:{
            lat:$('#lat').val(),
            lon:$('#lon').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            document.getElementById("icao").innerHTML = 'ICAO: ' + data.icao;
            document.getElementById("name").innerHTML = 'Name: ' + data.name;
            document.getElementById("lat_display").innerHTML = 'Latitude: ' + data.lat;
            document.getElementById("lon_display").innerHTML = 'Longitude: ' + data.lon;
            document.getElementById("elevation").innerHTML = 'Elevation: ' + data.elevation + ' ft';
            document.getElementById("country").innerHTML = 'Country: ' + data.country;
            document.getElementById("distance").innerHTML = 'Distance: ' + data.distance.toFixed(2) + ' nm';

            addAirportMarker(data.lat, data.lon);
        }
    });
});