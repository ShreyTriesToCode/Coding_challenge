import java.util.Arrays;

public class GreedyIntervalScheduling {

    public static void main(String[] args) {
        int[][] events = { { 1, 3 }, { 2, 4 }, { 0, 5 }, { 6, 7 } };
        System.out.println("Events: " + Arrays.deepToString(events));
        int[] schedule = greedyIntervalScheduling(events);
        System.out.println("Scheduled Events: ");
        for (int i : schedule) {
            System.out.print(i + " ");
        }
    }

    /**
     * This function schedules events using a greedy algorithm.
     *
     * @param events A 2D array of integers where each sub-array represents an event with its start and end time.
     * @return An integer array representing the scheduled events in ascending order of their start times.
     */
    public static int[] greedyIntervalScheduling(int[][] events) {
        // Sort the events based on their end times
        Arrays.sort(events, (a, b) -> a[1] - b[1]);

        int[] schedule = new int[events.length];
        for (int i = 0; i < events.length; i++) {
            if (i == 0 || events[i][0] >= events[i - 1][1]) {
                // Add the event to the schedule
                schedule[i] = events[i][0];
            }
        }

        return schedule;
    }
}