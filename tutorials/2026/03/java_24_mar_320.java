import java.util.HashMap;
import java.util.Map;

public class HashMapExample {

    // Create a new HashMap object
    public static void main(String[] args) {
        Map<String, Integer> hashMap = new HashMap<>();

        // Add key-value pairs to the map
        hashMap.put("John", 25);
        hashMap.put("Alice", 30);
        hashMap.put("Bob", 35);

        // Accessing a value from the map using its key
        System.out.println("John's age is: " + hashMap.get("John"));  // Output: John's age is: 25

        // Updating a value in the map
        hashMap.put("Alice", 31);
        System.out.println("Alice's updated age is: " + hashMap.get("Alice"));  // Output: Alice's updated age is: 31

        // Removing an element from the map
        hashMap.remove("Bob");
        System.out.println("Map after removing Bob: " + hashMap);  // Output: Map{John=25, Alice=31}

        // Check if a key exists in the map
        System.out.println("Does John exist in the map? " + hashMap.containsKey("John"));  // Output: Does John exist in the map? true

        // Get all keys from the map
        for (String key : hashMap.keySet()) {
            System.out.println(key);  // Output: John, Alice
        }

        // Get all values from the map
        for (int value : hashMap.values()) {
            System.out.println(value);  // Output: 25, 31
        }
    }
}