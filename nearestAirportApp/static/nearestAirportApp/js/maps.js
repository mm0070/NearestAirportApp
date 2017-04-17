var map;
var markers = [];

function initMap() {
    var londonHeathrow = {lat: 51.4723, lng: -0.4476};

    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 9,
        center: londonHeathrow,
        styles: [{"featureType":"administrative","elementType":"labels.text.fill","stylers":[{"color":"#444444"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2f2f2"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"saturation":-100},{"lightness":45}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#46bcec"},{"visibility":"on"}]}]
    });

    // This event listener will call addMarker() when the map is clicked.
    map.addListener('click', function(event) {
        deleteMarkers();
        addMarker(event.latLng);
        document.getElementById('lat').value = event.latLng.lat();
        document.getElementById('lon').value = event.latLng.lng();
    });
}

// Adds a marker to the map and push to the array.
function addMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map,
        icon: airplane_icon
    });
    markers.push(marker);
}

function addAirportMarker(airportLat, airportLng) {
    var marker = new google.maps.Marker({
        position: {lat: airportLat, lng: airportLng},
        map: map,
        icon: airport_icon
    });
    markers.push(marker);
}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
    setMapOnAll(null);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
    clearMarkers();
    markers = [];
}