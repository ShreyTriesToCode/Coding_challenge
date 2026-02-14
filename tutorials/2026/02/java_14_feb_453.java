import java.util.Arrays;

public class GreedyIntervalScheduling {
    // function to find max value
    public static int max(int a, int b) {
        return Math.max(a, b);
    }

    // function for greedy interval scheduling
    public static void schedule(int[] intervals) {
        // sort intervals based on end time
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        // initialize variables to keep track of end time and total profit
        int end = 0, totalProfit = 0;
        for (int[] interval : intervals) {
            if (interval[0] >= end) {
                end = interval[1];
                totalProfit += interval[2];
            }
        }
        // print the scheduled intervals and total profit
        System.out.println("Scheduled Intervals: ");
        for (int[] interval : intervals) {
            if (interval[0] == end) {
                System.out.print(interval[0] + " - " + interval[1] + "  Profit=" + interval[2]);
                System.out.print(", ");
            }
        }
        System.out.println("\nTotal Profit: " + totalProfit);
    }

    public static void main(String[] args) {
        int[][] intervals = { { 0, 30 }, { 5, 10 }, { 15, 20 } };
        schedule(intervals);
    }
}