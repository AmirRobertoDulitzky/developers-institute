// Daily Challenge: Stars

// Write a JavaScript program that recreates the pattern below
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

// Do this challenge twice: first by using one loop

let strarsString = "";

for (let i = 0; i < 6; i++) {
    strarsString += " *";
    console.log(strarsString);
}

// with array: (just to try)
let stars = [];

for (let i = 0; i < 6; i++) {
    stars.push("*");
    console.log(stars);
}

// then by using two nested for loops
let strarsString2 = "";

for (let i = 0; i < 6; i++) {
    for (let j = 0; j <= i; j++) {
        strarsString2 += " *";
    }
    strarsString2 += "\n";
}

console.log(strarsString2);  

