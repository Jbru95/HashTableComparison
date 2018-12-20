import random
import time
# Hash Table Class to compare speed


class HashTable:

    # constructor
    # @param size: hashTable size
    def __init__(self, size):
        self.size = size
        self.data = []
        for i in range(self.size):
            self.data.append([])

    # overloading index operator to return value associated with given key
    # @param key: string to index for value
    def __getitem__(self, key):
        bucket_array = self.data[self.__hash(key)]
        if bucket_array:  # true if something is found at that index
            for tup in bucket_array:
                if tup[0] == key:
                    return tup[1]
        else:
            return False

    # hash and compression function, returning an index in HashTable data from the key
    # @param key: string to hash and compress to find index to look up
    def __hash(self, key):
        hash_key = 7
        for char in str(key):
            hash_key += 10011*ord(char)

        return_index = hash_key % self.size
        return return_index

    def add(self, key, value):
        append_tup = (key, value)
        self.data[self.__hash(key)].append(append_tup)

    def delete(self, key):
        bucket_array = self.data[self.__hash(key)]
        if bucket_array:  # true if something is found at that index
            for tup in bucket_array:
                if tup[0] == key:
                    bucket_array.remove(tup)
        else:
            return False


def random_string():
    rand_str = ""
    for i in range(0,8):
        rand_str += chr(random.randint(1,127))
    return rand_str



ht = HashTable(1500000)

long_list = []
for i in range(1000000):
    long_list.append(i)
    ht.add(random_string(), i)

start_time_ary = time.time()  # start time before looking up elem in array

print(9857850 in long_list)

end_time_ary = time.time()

print("array lookup time" + str(end_time_ary - start_time_ary)) # display time difference: 0.08967447280883789


ht.add('kittycat', 69696969)  # add random key to look for into hash table

start_time_ht = time.time()  # start time before looking up elem in hash table

print(ht["kittycat"])

end_time_ht = time.time()

print("hashTable lookup time" + str(end_time_ht - start_time_ht))  # display time 0.0







