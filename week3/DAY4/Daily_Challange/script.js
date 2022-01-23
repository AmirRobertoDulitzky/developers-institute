// Daily Challenge: Not Bad

// 1. Create a variable called "sentence". 
// The value of the variable should be a string that contains the words “not” and “bad”

let sentence = "the movie is not too bad , do you not agree?";
console.log(sentence);
// 2. Create a variable called wordNot where it’s value is the first appearance of the substring “not”

sentanceArr = sentence.split(' ');

let wordNot;
let wordNotIndex;

for (i = 0; i < sentanceArr.length; i++) {
    switch (sentanceArr[i]) {
        case "not":
            wordNot = sentanceArr[i];
            wordNotIndex = sentanceArr.indexOf(wordNot);
            break;
    }
}

console.log(wordNot);
console.log(wordNotIndex);

// 3. Create a variable called wordBad where it’s value is the first appearance of the substring “bad” 

let wordBad;
let wordBadIndex;

for (i = 0; i < sentanceArr.length; i++) {
    switch (sentanceArr[i]) {
        case "bad":
            wordBad = sentanceArr[i];
            wordBadIndex = sentanceArr.indexOf(wordBad);
            break;
    }
}

console.log(wordBad);
console.log(wordBadIndex);

// 4. If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result
// 5. If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.

if (wordBadIndex > wordNotIndex) {
    let subString = sentanceArr.slice(wordNotIndex, wordBadIndex + 1);
    console.log(subString);
    let newSubString = "good";
    sentanceArr.splice(wordNotIndex, subString.length, newSubString);
    sentence = sentanceArr.join(" ");
}
console.log(sentence);
