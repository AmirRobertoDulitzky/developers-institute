// Exercise 3: Even Or Odd
// 1. Prompt the user for a number and save it to a variable

var number = parseInt(prompt("enter number"));
console.log(number);

// 2. Check whether the variable is even or odd.
// If it is even, display: “x is an even number”. Where x is the actual number the user chose.
// If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.

if (number % 2 == 0) {
    console.log(`${number} is an even number`);
} else {
    console.log(`${number} is an odd number`);
}

