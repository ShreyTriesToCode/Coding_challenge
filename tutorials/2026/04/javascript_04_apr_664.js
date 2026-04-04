// Greedy Interval Scheduling
// This algorithm schedules tasks in order of their end times to minimize the total time.

function nextGreatestEndTime(endTimes) {
    // Sorts end times in ascending order
    endTimes.sort((a, b) => a - b);
    return endTimes;
}

function greedyIntervalScheduling(endTimes) {
    // Selects tasks with earliest end times and checks if they do not overlap with the previously selected task
    for (let i = 0; i < endTimes.length - 1; i++) {
        if (endTimes[i + 1] > endTimes[i]) {
            return false;
        }
    }
    return true;
}

function scheduleIntervals(endTimes, startTimes) {
    // Combines the greedy interval scheduling result with task assignments
    let selectedTasks = [];
    for (let i = 0; i < endTimes.length; i++) {
        if (greedyIntervalScheduling([endTimes[i], ...startTimes[i]])) {
            selectedTasks.push(i);
        }
    }
    return [selectedTasks, startTimes[selectedTasks]];
}

// Example usage
const endTimes = [1, 2, 3, 4, 5];
const startTimes = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]];
let [selectedTasks, assignedStarts] = scheduleIntervals(endTimes, startTimes);
console.log(selectedTasks); // Prints: [4]
console.log(assignedStarts[selectedTasks[0]]);