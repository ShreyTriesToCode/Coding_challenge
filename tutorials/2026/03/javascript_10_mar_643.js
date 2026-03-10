// Greedy Interval Scheduling
// This algorithm solves the interval scheduling problem by selecting the interval that ends earliest.

// Function to find the maximum number of intervals that can be scheduled
function maxS scheduledIntervals(intervals) {
    // Sort the intervals by their end times
    intervals.sort((a, b) => a[1] - b[1]);
    // Initialize the count of scheduled intervals and the end time of the last scheduled interval
    let scheduledCount = 0;
    let lastEndTime = -Infinity;
    // Iterate over the sorted intervals
    for (let i = 0; i < intervals.length; i++) {
        // If the current interval does not conflict with the last scheduled interval, schedule it
        if (intervals[i][0] >= lastEndTime) {
            scheduledCount++;
            lastEndTime = intervals[i][1];
        }
    }
    return scheduledCount;
}

// Function to print the scheduled intervals
function printScheduledIntervals(intervals, scheduledCount) {
    let scheduledIntervals = [];
    // Iterate over the intervals and add the scheduled intervals to the list
    for (let i = 0; i < scheduledCount; i++) {
        scheduledIntervals.push(intervals[i]);
    }
    // Print the scheduled intervals
    console.log("Scheduled Intervals:");
    for (let i = 0; i < scheduledIntervals.length; i++) {
        console.log(`Interval ${i+1}: Start Time - ${scheduledIntervals[i][0]}, End Time - ${scheduledIntervals[i][1]}`);
    }
}

// Main function
function main() {
    // Define the intervals
    let intervals = [[1, 3], [2, 4], [3, 5], [6, 7], [8, 9]];
    // Find the maximum number of intervals that can be scheduled
    let scheduledCount = maxS scheduledIntervals(intervals);
    // Print the scheduled intervals
    printScheduledIntervals(intervals, scheduledCount);
}

// Call the main function
main();