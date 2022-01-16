
// 1. Create an array called colors where the value is a list of your five favorite colors.
let colors = ["black", "white", "red", "green", "blue"];

console.log(colors);

// 2. Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .

for (i = 0; i < colors.length; i++) {
    console.log(`My #${(i + 1)} choice is ${colors[i]}`);
}

// 3. Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”
console.log("Bonus:");
let suff = ["1st", "2nd", "3rd", "4th", "5th"];

for (i = 0; i < colors.length; i++) {
    console.log(`My #${suff[i]} choice is ${colors[i]}`);
}


