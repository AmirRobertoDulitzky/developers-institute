
// Part 1
let watchedSeries = ["black mirror", "money heist", "the big bang theory"];
console.log(watchedSeries);
// 1.
let watchedSeriesLength = watchedSeries.length;
console.log(watchedSeriesLength);

// 2.
let seriesPartOne = watchedSeries.slice(0, (watchedSeriesLength - 1));
console.log(seriesPartOne);

let seriesPartTwo = watchedSeries.slice((watchedSeriesLength - 1), (watchedSeriesLength));
console.log(seriesPartTwo);

let myWatchedSeries = `${seriesPartOne} and ${seriesPartTwo}`;

// 3.
console.log(`I wached ${watchedSeriesLength} series: ${myWatchedSeries}`);

// Part 2
// 1.
watchedSeries.splice(watchedSeries.indexOf("the big bang theory"), 1, "Friends");
console.log(watchedSeries);
// 2.
watchedSeries.push("gilmore girls");
console.log(watchedSeries);
// 3.
watchedSeries.splice(0, 0, "seinfeld");
console.log(watchedSeries);
// 4.
watchedSeries.splice(watchedSeries.indexOf("black mirror"), 1);

// 5.
console.log(seriesPartOne[1].charAt(2));

console.log(watchedSeries);


