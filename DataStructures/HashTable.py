# Name: Steven Holevas | ID: 001088230

class HashTable:
    """this hash table is a chaining hash table, to allow a small amount of space for storing data"""

    # constructor
    # has a size limit, makes a place to store the hash table values [list of lists] and the
    # number of elements currently in the array
    def __init__(self):
        self.size = 10
        self.hash_map = [[] for bucket in range(0, self.size)]
        self.number_of_elements = 0

    # creates a string format
    def __str__(self):
        string = "{}"
        return string.format(self.hash_map)

    # provides a hashed key by applying a mathimatical equation to each letter within the key
    def hash(self, key):
        hashed_key = 0
        for letters in key:
            hashed_key += ord(letters) * 64 - 2^ord(letters)
        hashed_key = hashed_key % self.size
        return hashed_key

    # inserts the value given into the hash table,
    # if the key already exists in the hash table, then it replaces the value
    # if the key does not exist, it hashes the key and enters the value

    # B3: SPACE TIME AND BIG-O
    # WORST CASE TIME COMPLEXITY: O(N) WHERE N IS THE # OF ITEMS IN EACH BUCKET [SHOULD AVERAGE O(1) THOUGH]
    # WORST CASE SPACE COMPLEXITY: O(N) WHERE N IS THE NUMBER OF ITEMS IN THE HASH TABLE
    def insert(self, key, value):
        hash_key = self.hash(key)
        key_exists = False
        bucket = self.hash_map[hash_key]

        # this is to allow for chaining to occur,
        # it enumerates through the current bucket within the hash table
        for item, key_value in enumerate(bucket):
            the_key, the_value = key_value

            # if the passed key is equal to the key_value already stored in the hash table
            if (key == the_key):
                key_exists = True
                break

        # if the key already exists, just replace the hash table value
        if (key_exists):
            bucket[item] = ((key, value))

        # else append it to the list in that bucket
        else:
            bucket.append((key, value))
            self.number_of_elements += 1

    # finds the value of an item given the key
    # WORST CASE TIME COMPLEXITY: O(N) WHERE N IS THE # OF ITEMS IN EACH BUCKET [SHOULD AVERAGE O(1) THOUGH]
    def find(self, key):
        # hash key of the given item
        hash_key = self.hash(key)
        # the list within the list called hash_map
        bucket = self.hash_map[hash_key]

        # if the bucket just has one item O(1)
        if (len(bucket) == 1):
            the_key, the_value = bucket[0]
            return the_value

        # else go into O(n) loop
        for key_value in bucket:
            the_key, the_value = key_value
            if (key == the_key):
                return the_value

        # if it does not find a value, through an error
        raise KeyError("does not exist")

    # WORST CASE TIME COMPLEXITY: O(N) WHERE N IS THE # OF ITEMS IN EACH BUCKET [SHOULD AVERAGE O(1) THOUGH]
    # removes a value in the list given the key
    def remove(self, key):
        # hashes key
        hash_key = self.hash(key)
        # finds bucket based on hashed_key
        bucket = self.hash_map[hash_key]
        the_key = None
        the_value = None

        # if it is just that item in the bucket, pop it O(1)
        if (len(bucket) == 1):
            the_key, the_value = bucket[0]
            bucket.pop()

        # otherwise, iterate through and pop the value when it is reached
        else:
            for key_value in bucket:
                the_key, the_value = key_value
                if (key == the_key):
                    bucket.pop()
                    break

        # if there is actually a value
        if (the_value != None):
            self.number_of_elements -= 1

        # otherwise, throw an exception
        else:
            raise ValueError("value does not exist")

        # return the value remvoved
        return the_value



    # this function traverses and prints out all the values in the hash table
    # WORST CASE TIME COMPLEXITY: O(N) WHERE N IS THE # OF ITEMS IN THE TABLE
    def traverse(self):
        # declared variables
        hash_map = self.hash_map
        the_key = None
        the_value = None

        # for every bucket in the hash map iterate through
        for buckets in hash_map:
            # if the bucket is empty, just skip the next steps and try again on the next bucket
            if (len(buckets) == 0):
                continue

            # if the value is 1, just print the first item
            elif (len(buckets) == 1):
                the_key, the_value = buckets[0]
                print(the_value)

            # otherwise, iterate through the whole bucket within the hash table
            elif(len(buckets) > 1):
                for key_value in buckets:
                    the_key, the_value = key_value
                    print(the_value)

    # returns the number of elements
    def get_number_of_elements(self):
        return self.number_of_elements

    # allows the future programmer to write the hash table in the format of an actual hash table when setting a value
    # example: HashTable["Hi"] = 26
    def __setitem__(self, key, value):
        return self.insert(key, value)

    # allows the future programmer to treat the hash table in the format of an actual hash table when retrieving values
    # example: Hashtable["Hi"]
    def __getitem__(self, key):
        return self.find(key)
