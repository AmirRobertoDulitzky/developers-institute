// 1. Prompt the user for a number.
var number = parseInt(prompt("enter number"));
console.log(number);

// 2. While the number is smaller than 10 continue asking the user for a new number.

while (number < 10)
{
    number = parseInt(prompt("enter number")); 
    console.log(number);
}

// ---------------------------------------------------

// code seems shorter when using "Do While Loop":

// do {
// var number = parseInt(prompt("enter number"));
// console.log(number);
// }
// while (number < 10);