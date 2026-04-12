# Hash Map in Python
# A Hash Map is a data structure that stores key-value pairs in an array using a hash function.

class HashMap:
    def __init__(self, size=10):
        # Initialize the hashmap with a given size
        self.size = size
        # Create a list of empty buckets
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        # Calculate the hash value using the built-in hash function and modulus operator
        return hash(key) % self.size

    def put(self, key, value):
        # Find the bucket for the given key
        index = self._hash(key)
        # If the bucket is empty, create a new entry
        if not self.buckets[index]:
            self.buckets[index] = [(key, value)]
        else:
            # If the key already exists, update its value
            for i, (k, v) in enumerate(self.buckets[index]):
                if k == key:
                    self.buckets[index][i] = (key, value)
                    break

    def get(self, key):
        # Find the bucket for the given key
        index = self._hash(key)
        # If the bucket is empty, return None
        if not self.buckets[index]:
            return None
        else:
            # Iterate through the entries in the bucket
            for k, v in self.buckets[index]:
                if k == key:
                    return v

    def remove(self, key):
        # Find the bucket for the given key
        index = self._hash(key)
        # If the bucket is empty, return None
        if not self.buckets[index]:
            return None
        else:
            # Iterate through the entries in the bucket
            for i, (k, v) in enumerate(self.buckets[index]):
                if k == key:
                    del self.buckets[index][i]
                    break

    def display(self):
        # Display the contents of the hashmap
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: ", end="")
            for k, v in bucket:
                print(f"{k} : {v}", end=" ")
            print()

# Create a new hashmap with size 10
hashmap = HashMap(10)

# Add some key-value pairs to the hashmap
hashmap.put("John", "Age 30")
hashmap.put("Alice", "Age 25")
hashmap.put("Bob", "Age 40")

# Display the contents of the hashmap
print("Hashmap Contents:")
hashmap.display()

# Get a value from the hashmap
print("\nGetting value for key 'John': ", hashmap.get("John"))

# Remove a key-value pair from the hashmap
hashmap.remove("Alice")

# Display the updated contents of the hashmap
print("\nUpdated Hashmap Contents:")
hashmap.display()