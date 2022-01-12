let birthYear = 1980;

let futureYear = 2041;

let futureAge = futureYear - birthYear ;

// let Answer = "I will be " + futureAge + " in " + futureYear + " .";
let Answer = `I will be ${futureAge} in ${futureYear}.`;

console.log(Answer);

document.getElementById("bt-1").onclick = 
function(){
    alert(Answer);
}