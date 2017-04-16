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
            document.getElementById("icao").innerHTML = 'Nearest airport ICAO: ' + data.icao;
            document.getElementById("name").innerHTML = 'Nearest airport Name: ' + data.name;
        }
    });
});