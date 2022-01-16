let pets = ["cat", "dog", "fish","rabbit","cow"];

console.log(pets[1]);

// adding "horse" to the end:
pets.push("horse");

// adding "horse" to the begining:
// pets.unshift("horse");

// adding "horse" after the 2nd element (the dog): 
// pets.splice(2,0,"horse"); 

console.log(pets);

let rabbitIndex = pets.indexOf('rabbit');
console.log("rabbit Index is: " + rabbitIndex);

pets.splice(rabbitIndex,1);

// after removing rabbit:
console.log(pets);

console.log(`Array length is: ${pets.length}`);



