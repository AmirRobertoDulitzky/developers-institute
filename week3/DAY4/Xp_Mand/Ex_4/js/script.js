// Exercise 4: Group Chat

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

// console.log the online users acording to how many are online 

switch (users.length) {
    case 1:
        console.log(`${users[0]} is online`);
        break;
    case 2:
        console.log(`${users[0]} and ${users[1]} are online`);
        break;
    default:
        console.log(`${users[0]} and ${users[1]} and ${users.length - 2} more are online`);
}

