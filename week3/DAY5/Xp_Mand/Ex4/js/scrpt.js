// 1. Copy and paste this object to your Javascript file.

let building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
};

// 2. Console.log the number of floors in the building.

console.log(`number of floors: ${building.numberOfFloors}`);

// 3. Console.log how many apartments are on the floors 1 and 3

console.log(`No. of apartments of floor 1: ${building.numberOfAptByFloor.firstFloor}`);
console.log(`No. of apartments of floor 3: ${building.numberOfAptByFloor.thirdFloor}`);

// 4. Console.log the name of the second tenant and the number of rooms he has in his apartment.

console.log(`${building.nameOfTenants[1]} the 2nd tentant has ${building.numberOfRoomsAndRent.dan[0]} rooms`);

// 5. Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
console.log(building.numberOfRoomsAndRent.dan[1]);

if (building.numberOfRoomsAndRent.sarah[1] +
    building.numberOfRoomsAndRent.david[1] >
    building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}
console.log(building.numberOfRoomsAndRent.dan[1]);

//----------------------------------------- NOTE :  ----------------------------------
// Is it better to do this in terms of ease of readebility? :  

// let sarahRent = building.numberOfRoomsAndRent.sarah[1];
// let davidRent = building.numberOfRoomsAndRent.david[1];
// let danRent = building.numberOfRoomsAndRent.dan[1];

// if (sarahRent + davidRent > danRent) {
//     building.numberOfRoomsAndRent.dan[1] = 1200;
// }

