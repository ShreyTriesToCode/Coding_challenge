// Greedy Interval Scheduling Algorithm
// This algorithm works by selecting the earliest possible start time for each activity,
// ensuring that we don't schedule two activities on the same day.

class Activity {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }
}

class Scheduler {
    constructor() {
        this.activities = [];
    }

    // Add an activity to the scheduler
    addActivity(activity) {
        this.activities.push(activity);
    }

    // Sort activities by end time
    sortActivities() {
        this.activities.sort((a, b) => a.end - b.end);
    }

    // Initialize variables for greedy algorithm
    initializeGreedyVariables() {
        let lastEndTime = 0;
        let schedule = [];

        // Iterate through each activity in sorted order
        for (let i = 0; i < this.activities.length; i++) {
            if (this.activities[i].start >= lastEndTime) {
                // Add to the current day
                schedule.push(this.activities[i]);
                lastEndTime = Math.max(lastEndTime, this.activities[i].end);
            }
        }

        return schedule;
    }

    // Greedy interval scheduling function
    greedyIntervalScheduling() {
        this.sortActivities();
        let schedule = this.initializeGreedyVariables();

        return schedule;
    }
}

// Test the scheduler with some sample activities
let scheduler = new Scheduler();
scheduler.addActivity(new Activity(1, 4));
scheduler.addActivity(new Activity(2, 5));
scheduler.addActivity(new Activity(3, 6));

// Run greedy interval scheduling on the activities
let schedule = scheduler.greedyIntervalScheduling();

console.log(schedule);