public class KMPSearch {

    // Function to compute prefix function
    private static int[] computePrefixFunction(String str) {
        int n = str.length();
        int[] pi = new int[n];
        
        // Initialize first element as 0
        pi[0] = -1;
        
        // Compute prefix function values
        for (int i = 1; i < n; i++) {
            int j = pi[i-1];
            
            // If current character match with character at j+1 position, then update pi[i]
            while (j >= 0 && str.charAt(i) != str.charAt(j+1)) {
                j = pi[j];
            }
            if (str.charAt(i) == str.charAt(j+1)) {
                j += 1;
            }
            pi[i] = j;
        }
        
        return pi;
    }

    // Function for KMP algorithm
    public static int kmpSearch(String text, String pattern) {
        int m = pattern.length();
        int n = text.length();
        int[] pi = computePrefixFunction(pattern);
        
        int j = 0; // index to track current position in pattern
        for (int i = 0; i < n; i++) {
            while (j >= 0 && text.charAt(i) != pattern.charAt(j+1)) {
                j = pi[j];
            }
            if (text.charAt(i) == pattern.charAt(j+1)) {
                j += 1;
            }
            
            // If entire pattern is found, return index
            if (j == m - 1) {
                return i - (m-1);
            }
        }
        
        // Pattern not found in text
        return -1;
    }

    public static void main(String[] args) {
        String text = "ABABDABACDABABCABAB";
        String pattern = "ABABCABAB";
        int index = kmpSearch(text, pattern);
        
        if (index != -1) {
            System.out.println("Pattern found at index: " + index);
        } else {
            System.out.println("Pattern not found in text.");
        }
    }
}