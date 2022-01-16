let people = ["Greg", "Mary", "Devon", "James"];

console.log(people);

// ----------------- Part I - Review About Arrays ------------------------

// 1. remove first element.

// methode a:
// people.shift();

// methode b:
people.splice(0, 1);

console.log(people);

// 2.replace james with jason.

people.splice(2, 1, "Jason");

console.log(people);

// 3.add my name to the end of the Array.

people.push("Amir");

console.log(people);

// 4.consol log Mary's index.

console.log(`the index of Mary is ${people.indexOf("Mary")}`);

// 5.create a copy of the Array.
// disclude mary and your name.

let peopleCopy = people.slice(1, -1);

console.log(peopleCopy);

// 6.Write code that gives the index of “Foo”. Why does it return -1 ?

console.log(people.indexOf("Foo"));
// when we ask the index of a non-existing element in an array the answer will be -1

// 7.create var "last" which gives the last element of the array.

let last = people[(people.length - 1)];

console.log(`the last element is ${last}`);

// ------------------------ Part II - Loops ----------------------

// 1. Using a loop, iterate through the people array and console.log each person.
console.log("Part 1 - log through the names:");
for (i = 0; i < people.length; i++) {
    console.log(`element ${i} is ${people[i]}`);
}

// 2. Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .

console.log("Part 2 - log through the names and exit after Jason:");
for (i = 0; i < people.length; i++) {

    if (i === people.indexOf("Jason") + 1) {
        break;
    }
    console.log(`element ${i} is ${people[i]}`);
}

