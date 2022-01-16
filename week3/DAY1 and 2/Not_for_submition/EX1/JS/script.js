let addressNumber = 5;

let addressStreet = "Ha halutzim";

let country = "Israel";

let globalAddress = "I live in " + addressStreet + " " + addressNumber + " ,in " + country;

console.log(globalAddress);

document.getElementById("bt-1").onclick = 
function(){
    alert(globalAddress);
}