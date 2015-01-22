# RoboHash
RoboHash is a HashTable implementation that provides constant time lookups and O(N) insertion time.
It uses Open Addressing with linear probing for Hash collision resolution.
Data is stored in a dynamically resizing array that will double in size when 70% of the array is filled.

The requirements specified are as follows:
* Design and implement a fixed size hash table that resolves collisions by efficiently finding an unoccupied spot in the table.
* It may be necessary to grow the size of the table.
* Keep statistics on the frequency of collisions and the distribution of the number of collisions for all inserts.
* Demonstrate that items can be reliably retrieved from the table.
* You will need to provide some means for items to be inserted into the table, to inspect the contents of the table and to print the statistics.
* Please provide a comprehensive test suite to validate all edge cases. Provide a written description of how the algorithm works.

# Initialization
RoboHash initializes by creating an array of the size specified in the constructor (or defaults to 1117).

# Insertion
Before an item is inserted the storage array will expand if needed (see following section).
The item's key is then hashed to attempt to determine the bin to store the item in. If the bin is empty the item will be stored there.
If the bin is occupied the algorithm will begin linear probing to find the next available slot.

# Array Expansion
It will be expanded if the ratio of hashed items to storage array size is greater than the "storage_threshold" parameter (by default, 70%).
An array expansion will be done by creating a new Array twice the size as the original, and then inserting the existing items into the new array.

# Retrieval
An item is retrieved in a very similar manner as insertion. The key will be hashed to determine the first slot to look.
If the slot is empty, then the key does not exist in the hash table. If an item exists, it is then checked to make sure the key matches the one being requested.
If the key does not match then linear probing will begin until either the key is found or an empty slot is encountered - indicating the requested key does not exist.

# Usage
```python

array_size = 1117 # the size of the table to start with, will double when reaching storage_threshold
storage threshold = 0.7 # the ratio of hashed items to buckets. Array will double when threshold is exceeded
h = RoboHash(array_size,threshold)
h.insert(1, "foo")
res = h.get(1)
h.pretty_print()
h.stats.pretty_print()
h.stats.print_distribution(h.storage, 10)
```