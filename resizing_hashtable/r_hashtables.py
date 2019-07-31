

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
  
    for character in string:
        hash = ((hash << 5) + hash) + ord(character)
   
    return hash % max


def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    print(f'Inserting key:{key} at index: {index}')
    current = hash_table.storage[index]

    while current is not None and current.key != key:
        current = current.next
    
    if current is None:
        newPair = LinkedPair(key, value)

        oldHead = hash_table.storage[index]
        hash_table.storage[index] = newPair.next = oldHead

        if newPair.next is None:
            hash_table.count +=1
    else:
        current.value = value



def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]
    prev_pair = None
    
    if current_pair is not None:
        while current_pair is not None and current_pair.key != key:
            prev_pair = current_pair
            current_pair = current_pair.next

        if prev_pair is None and current_pair.key == key:
            hash_table.storage[index] = None
            hash_table.count +=1
        elif current_pair is None:
            prev_pair = None
        else:
            prev_pair.next = None
        
    else:
        print(f'Error: {key} not found')
        return None




# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    
    current = hash_table.storage[index]

    if current is not None:
        while current is not None and current.key != key:
            current = current.next
        
        if current is None:
            print(f'Error {key} not found.')
        else:
            return current.value
    
    else:
        return None


def hash_table_resize(hash_table):
    new_hash_table = HashTable(hash_table.capacity * 2)

    for x in range(:hash_table.count):
        print(x)

        while current_pair is not None:
            hash_table_insert(new_hash_table, current_pair.key, current_pair.value)
            current_pair = current_pair.next

    return new_hash_table

def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
