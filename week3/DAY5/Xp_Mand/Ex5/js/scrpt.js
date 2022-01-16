// 1. Create an object called family with a few key value pairs.

let family = {
    father: "Fred",
    wife: "Wilma",
    daughter: "Pebbles"
};

console.log(family);

// 2. Using a for loop, console.log the keys of the object.
let keys = Object.keys(family);

for (let i = 0; i < keys.length; i++) {
    console.log(keys[i]);  
}

// 3. Using a for loop, console.log the values of the object.

let values = Object.values(family);

for (let i = 0; i < values.length; i++) {
    console.log(values[i]);  
}