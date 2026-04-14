# Question: Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:
'''
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
'''



class TimeMap:
    def __init__(self):
        # Define the store
        self.store = {}

    # TC: O(1)       SC: O(N)
    def set(self, key: str, value: str, timestamp: int) -> None:
        # Check for key in store
        if key not in self.store:
            # Key not found: create arr
            self.store[key] = []
        # Key found: append in existing key tuple pair
        self.store[key].append((timestamp, value))    
    

    # TC: O(log(n))       SC: O(1)
    def get(self, key: str, timestamp: int) -> str:
        # Key not in store
        if key not in self.store:
            # Exit and return ""
            return ""
        # Store all keys in arr
        arr = self.store[key]
        # Define BS Variables
        l, r = 0, len(arr)-1
        res = ""
        # Start condition
        while l <= r:
            # Define mid var
            m = (l+r) // 2
            # Check for timestamp at mid with prev
            if arr[m][0] <= timestamp:
                # Update res wrt value
                res = arr[m][1]
                # Update left
                l = m + 1
            else:
                # Update right
                r = m - 1
        # Return val
        return res





# Custom Test Cases
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
q = TimeMap()
print(q)