var slider1 = document.getElementById("priceRange");
var slider2 = document.getElementById("bedRange");
var slider3 = document.getElementById("bathRange");

var output1 = document.getElementById("price");
var output2 = document.getElementById("beds");
var output3 = document.getElementById("baths");

output1.innerHTML = slider1.value;
output2.innerHTML = slider2.value;
output3.innerHTML = slider3.value;

slider1.oninput = function() {
  output1.innerHTML = new Intl.NumberFormat().format(parseInt(this.value));
}

slider2.oninput = function() {
  output2.innerHTML = this.value;
}

slider3.oninput = function() {
  output3.innerHTML = this.value;
}