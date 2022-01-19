window.onload = getMyLocation;

function displayError(error) {
    let errorTypes = {
        0: "Unknown error",
        1: "Permission denied by user",
        2: "Position is not available",
        3: "Request timed out"
    };
    let errorMessage = errorTypes[error.code];
    if (error.code == 0 || error.code == 2) {
        errorMessage = errorMessage + " " + error.message;
    }
    let div = document.getElementById("location");
    div.innerHTML = errorMessage;
}

let map;
function showMap(coords) {
    let googleLatAndLong = new google.maps.LatLng(coords.latitude, coords.longitude);
    let mapOptions = {
        zoom: 15,
        center: googleLatAndLong,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    let mapDiv = document.getElementById("map");
    map = new google.maps.Map(mapDiv, mapOptions);

    let title = "Animal location";
    let content = "Your animal is here: " + coords.latitude + ", " + coords.longitude;
    addMarker(map, googleLatAndLong, title, content);
}

function displayLocation(position) {
    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;
    let now = new Date();
    let hours = now.getHours();
    let minutes = now.getMinutes();

    let yourLocation = document.getElementById("yourLocation");
    yourLocation.innerHTML = "동물의 위치는 위도: " + latitude + ", 경도: " + longitude;

    let log = document.createElement('li');
    log.innerHTML = "동물의 위치는 위도: " + latitude + ", 경도: " + longitude + "<br>" + "시간 : " + hours + "시 " + minutes + "분";
    document.getElementById('logParent').appendChild(log);

    if(map == null) {
        showMap(position.coords);
    } else {
        scrollMapToPosition(position.coords);
    }
}

function addMarker (map, latlong, title, content) {
    let markerOptions = {
        position: latlong,
        map: map,
        title: title,
        clickable: true
    };

    let marker = new google.maps.Marker(markerOptions);

    let infoWindowOptions = {
        content: content,
        position: latlong
    };

    let infoWindow = new google.maps.InfoWindow(infoWindowOptions);

    google.maps.event.addListener(marker, "click", function () {
        infoWindow.open(map);
    });
}

function getMyLocation() {
    if (navigator.geolocation) {
        let watchButton = document.getElementById("watch");
        watchButton.onclick = watchLocation;
        let clearWatchButton = document.getElementById("stopWatch");
        clearWatchButton.onclick = clearWatch;
    }
    else {
        alert("실패");
    }
}

let watchId = null;

function watchLocation() {
    watchId = navigator.geolocation.watchPosition(displayLocation, displayError);
    console.log(watchId);
}

function clearWatch() {
    if (watchId) {
        navigator.geolocation.clearWatch(watchId);
        watchId = null;
        console.log(watchId);
    }
}

function  scrollMapToPosition(coords) {
    let latitude = coords.latitude;
    let longitude = coords.longitude;
    let latlong = new google.maps.LatLng(latitude, longitude);

    map.panTo(latlong);

    addMarker(map, latlong, "Your animal's location", "Animal moved to: " + latitude + ", " + longitude);
}