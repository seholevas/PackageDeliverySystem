class HashTable():
    def __init__(self):
        self.size = 10
        self.hash_map = [[] for bucket in range(0,self.size)]
        self.number_of_elements = 0
        # print(self.hash_map)

    def hash(self, key):
        hashed_key = key %  self.size
        return hashed_key

    def insert(self, key, value):
        hash_key = self.hash(key)
        key_exists = False
        bucket = self.hash_map[hash_key]

        #chaining
        for item, key_value in enumerate(bucket):
            the_key, the_value = key_value

            if(key == the_key):
                key_exists = True
                break

        if(key_exists):
            bucket[item] = ((key, value))

        else:
            bucket.append((key,value))

    def find(self, key, value):
        hash_key = self.hash(key)
        bucket = self.hash_map[hash_key]

        for key_value in bucket:
            the_key, the_value = key_value
            if(key == the_key):
                return value
            else:
                raise KeyError("does not exist")


H = HashTable()

H.insert(10, 10)
H.insert(20,20)
H.insert(3, 3)

print(H.hash_map)