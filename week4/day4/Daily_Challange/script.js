// Daily Challenge: 99 Bottles Of Beer

function bottles() {
    let bottlesStart = +prompt("How many bottles?");
    console.log(bottlesStart);
    let dec = 1;
    let bottlesEnd = bottlesStart;
    for (let i = 0; i < bottlesStart / dec ; i++) {
        console.log(`${bottlesEnd} bottles of beer on the wall`);
        bottlesEnd -= dec;
    }
}

bottles();