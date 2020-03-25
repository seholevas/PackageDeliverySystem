class HashTable():

    """built a rudimentary basic hashtable in order to practice building one from scratch."""
    def __init__(self):
        #default size
        self.size = 10
        self.hash_map = [[] for bucket in range(0,self.size)]
        self.number_of_elements = 0

    # hashes the key value (in the case of packages, it hashes the package id)
    def hash(self, key):
        hashed_key = key %  self.size
        return hashed_key

    # inserts a key value pair into the hashtable.
    def insert(self, key, value):
        hash_key = self.hash(key)
        key_exists = False
        bucket = self.hash_map[hash_key]

        #chaining the key value pair into the hashtable.
        for item, key_value in enumerate(bucket):
            the_key, the_value = key_value

            # if the key exists, break out of the for loop.
            if(key == the_key):
                key_exists = True
                break

        if(key_exists):
            bucket[item] = ((key, value))

        else:
            bucket.append((key,value))

    # finds a key value pair in this chaining hashtable.
    def find(self, key, value):
        hash_key = self.hash(key)
        bucket = self.hash_map[hash_key]

        for key_value in bucket:
            the_key, the_value = key_value
            if(key == the_key):
                return value
            else:
                raise KeyError("does not exist")