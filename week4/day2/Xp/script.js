// ---------------------------- Exercise 1 : Information -------------------------------

console.log("\nExercise 1 - Information :\n ");

function infoAboutMe() {
    console.log("my name is Elvis Im 87 years old my favirite color is Gold");
}

infoAboutMe();

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`your name is ${personName}, you are ${personAge} years old and your favorite color is ${personFavoriteColor}`);
}

infoAboutPerson("Prince", 64, "Purple");
infoAboutPerson("David", 45, "Blue");

// ------------------------------- Exercise 2 : Tips ----------------------------------

console.log("\nExercise 2 - Tips :\ncall the function calculateTip() at the bottom of Ex2 to check the Ex.\n ");

let bill;

function calculateTip() {
    bill = +prompt("how much is the bill?");
    if (bill > 0 && bill < 50) {
        console.log(`for ${bill}$ the tip is ${Number((bill * 0.2).toFixed(1))}$ . Total is ${Math.round(bill * 1.2)}$`);

    } if (bill >= 50 && bill <= 200) {
        console.log(`for ${bill}$ the tip is ${Number((bill * 0.15).toFixed(1))}$. Total is ${Math.round(bill * 1.15)}$`);

    } else if (bill > 200) {
        console.log(`for ${bill}$ the tip is ${Number((bill * 0.1).toFixed(1))}$. Total is ${Math.round(bill * 1.1)}$`);
    }
}

// call function to check Ex 2:
// calculateTip();

// ---------------------------- Exercise 3 : Find The Numbers Divisible By 23 ------------

function isDivisible() {
    let Divis = [];
    for (let i = 0; i < 500; i++) {
        if (i % 23 == 0) {
            Divis.push(i);
        }
    }

    let sum = 0;
    // console.log("Outcome:", Divis);
    console.log(`Outcome: ${Divis}`);

    for (let i = 0; i < Divis.length; i++) {
        sum += Divis[i];
    }
    // console.log("Sum: ", sum);
    console.log(`Sum: ${sum}`);
}

isDivisible();