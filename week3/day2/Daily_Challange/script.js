// Daily Challenge: JS Arrays & Methods

// ---------------------------- Exercise 1: -----------------------------------

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log(fruits);

// 1. Remove Banana from the array

fruits.shift();
console.log(fruits);

// 2. Sort the array in alphabetical order

fruits.sort();
console.log(fruits);

// 3. Add “Kiwi” to the end of the array

fruits.unshift("Kiwi");
console.log(fruits);

// 4. Remove “Apples” from the array. Don’t use the same method as in part 1

fruits.splice(1,1);
console.log(fruits);

// 5. Sort the array in reverse order. (Not alphabetical, but reverse the current Arra

fruits.reverse();
console.log(fruits);

// ----------------------------- Exercise 2: ----------------------------------

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

// 1. Access and then console.log “Oranges”

let favFrouit = moreFruits[1][1];
console.log(favFrouit);

// Or:

console.log(moreFruits[1][1]);