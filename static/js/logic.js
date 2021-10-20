var myMap = L.map("map", {
    center: [31.35, -96.25, 0.2],
    zoom: 5
});
  
// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

d3.json("/data").then(function(data) {
    // console.log(data);
    // console.log(data.map(x => x.LATITUDE)

    var heatArray = data.map(ufo => [ufo.LATITUDE, ufo.LONGITUDE]);
    // console.log(heatArray)

    var heat = L.heatLayer(heatArray, {
        radius: 20,
        blur: 35
    }).addTo(myMap);

});

