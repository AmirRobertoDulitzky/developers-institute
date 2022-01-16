let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
};

// 1. console.log “my name is Rudolf the raindeer”:

// without a loop:

let keys = Object.keys(details);

let values = Object.values(details);

console.log(`${keys[0]} ${values[0]} ${keys[1]} ${values[1]} ${keys[2]} ${values[2]}`);

// with a for loop and a new array (need "keys" and "values"):
let detailsArr = [];

for (let i = 0; i < keys.length; i++) {
    detailsArr.push(keys[i]);
    detailsArr.push(values[i]);
}

console.log(detailsArr.join(' '));

// with a  for loop and a new array (no need for "keys" and "values"):

let detailsArr2 = [];

for (let x in details) {
    detailsArr2.push(x);
    detailsArr2.push(details[x]);
}

console.log(detailsArr2.join(' '));

