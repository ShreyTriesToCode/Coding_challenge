import java.util.Arrays;

public class GreedyIntervalScheduling {
    // Function to find the minimum number of intervals that cover all events
    public static int minInterval(int[] start, int[] end) {
        // Sort the events by their end time
        for (int i = 0; i < start.length; i++) {
            for (int j = i + 1; j < start.length; j++) {
                if (start[i] > start[j]) {
                    int temp = start[i];
                    start[i] = start[j];
                    start[j] = temp;
                    temp = end[i];
                    end[i] = end[j];
                    end[j] = temp;
                }
            }
        }
        
        // Initialize variables to keep track of the end time of the last covered event and the count of intervals
        int lastEnd = end[0];
        int count = 1;
        
        // Iterate over the sorted events
        for (int i = 1; i < start.length; i++) {
            // If the current event starts after the last covered event ends, update the last end time and increment the count
            if (start[i] >= lastEnd) {
                lastEnd = end[i];
                count++;
            }
        }
        
        // Return the minimum number of intervals that cover all events
        return count;
    }

    public static void main(String[] args) {
        // Example usage
        int[] start = {1, 2, 3, 4, 5};
        int[] end = {2, 3, 4, 5, 6};
        System.out.println("Minimum number of intervals: " + minInterval(start, end));
    }
}