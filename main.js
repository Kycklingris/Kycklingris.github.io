var data = [
  {
    name: "Subway",
    location: "Odenplan",
    review: "4.5/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "10/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway7",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "Odenplan",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  }
  
];

var id = 1;

data.forEach(res => {
    let card = document.createElement("div");
  card.classList.add("card");
  card.id = "card" + parseInt(id);

    let header = document.createElement("H2")
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
    let reviewtmp = document.createTextNode('review:' + res.review);
    review.appendChild(reviewtmp);
    card.appendChild(review);

  id++;



    let container = document.querySelector("#container");
    container.appendChild(card);
});