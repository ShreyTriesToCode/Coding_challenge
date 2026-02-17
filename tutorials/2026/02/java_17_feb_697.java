import java.util.HashMap;
import java.util.Map;

public class StringHashing {

    // Define the hash function to calculate the hash value of a string
    public static int stringHash(String str) {
        int hashValue = 0;
        for (char c : str.toCharArray()) {
            // Convert each character to its ASCII value and add it to the hash value
            hashValue += Character.getNumericValue(c);
        }
        return hashValue;
    }

    // Define a method to find collisions by using separate chaining
    public static Map<Integer, Integer> stringHashing(String str) {
        int size = 10; // Choose an initial size for the hash table
        Map<Integer, Integer> hashTable = new HashMap<>();

        while (true) {
            int hashValue = stringHash(str);
            if (!hashTable.containsKey(hashValue)) {
                // If the hash table doesn't contain this key, add it with a unique value
                hashTable.put(hashValue, str.hashCode());
                break;
            } else {
                // If the hash table already contains this key, increment the size of the hash table
                size += 1;
                while (hashTable.containsKey(hashValue)) {
                    hashValue = (stringHash(str) + hashValue) % size;
                }
                hashTable.put(hashValue, str.hashCode());
            }
        }

        return hashTable;
    }

    public static void main(String[] args) {
        String str1 = "Hello";
        String str2 = "World";

        System.out.println("Hash value of '" + str1 + "' is: " + stringHash(str1));
        System.out.println("Hash value of '" + str2 + "' is: " + stringHash(str2));

        Map<Integer, Integer> hashTable = stringHashing(str1);
        for (Map.Entry<Integer, Integer> entry : hashTable.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}