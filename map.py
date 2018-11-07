class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def hash(self, key, size):
        return key % size
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size
    
        

