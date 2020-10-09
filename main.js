fetch('./data.json')
  .then(function (resp) {
    return resp.json()
  })
  .then(function (data) {

    data.forEach((res) => {
      var value = Math.floor(Math.random() * 10);
      res["review"] = value;
    });

    var id = 1;

    data.forEach((res) => {
      let card = document.createElement("div");
      card.classList.add("card");
      card.id = "card" + parseInt(id);

      let header = document.createElement("H2");
      header.classList.add("header");
      let name = document.createTextNode(res.name);
      header.appendChild(name);
      card.appendChild(header);

      let address = document.createElement("p");
      address.classList.add("address");
      let location = document.createTextNode(res.location);
      address.appendChild(location);
      card.appendChild(address);

      let review = document.createElement("p");
      review.classList.add("review");
      let reviewtmp = document.createTextNode("review:" + res.review);
      review.appendChild(reviewtmp);
      card.appendChild(review);

      id++;

      let container = document.querySelector("#container");
      container.appendChild(card);
    });
  })





var map = new ol.Map({
  target: "map",
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM(),
    }),
  ],
  view: new ol.View({
    center: ol.proj.fromLonLat([18.04724, 59.340148]),
    zoom: 15,
  }),
});

var iconStyle = new Style({
  image: new Icon({
    src: "school-marker.png",
  }),
});

 var layer = new ol.layer.Vector({
   source: new ol.source.Vector({
     features: [
       iconStyle,
       new ol.Feature({
         geometry: new ol.geom.Point(ol.proj.fromLonLat([18.04618, 59.337579])),
       }),
     ],
   }),
 });
 map.addLayer(layer);
