let data = [
  {
    name: "Subway",
    location: "description",
    review: "4.5/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "description",
    review: "10/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "description",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
  },
  {
    name: "Subway",
    location: "description",
    review: "7/10",
    annexet: "5min",
    craford: "10min",
    },
  
];

data.forEach(res => {
    let card = document.createElement("div");
    card.classList.add("card");

    let header = document.createElement("H2")
    header.classList.add("header");
    let name = document.createTextNode(res.name);
    header.appendChild(name);
    card.appendChild(header);


    let address = document.createElement("p");
    address.classList.add("address");
    let location = document.createTextNode('Location:' + res.location + ', ');
    address.appendChild(location);
    card.appendChild(address);

    let review = document.createElement("p");
    review.classList.add("review");
    let reviewtmp = document.createTextNode('review:' + res.review);
    review.appendChild(reviewtmp);
    card.appendChild(review);






    let container = document.querySelector("#container");
    container.appendChild(card);
});