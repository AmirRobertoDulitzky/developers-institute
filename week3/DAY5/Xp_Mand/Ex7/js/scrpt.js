
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// Console.log the name of their secret society. The output should be “ABJKPS”:

let secretName = [];

for (let x in names) {
    secretName.push(names[x].charAt(0));
}

secretName = secretName.sort().join('');

console.log(secretName);