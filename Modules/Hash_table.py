#Hash table skeleton
class Hash_table:
    def __init__(self, size=40):
        self.size = size
        self.table = [[] for _ in range(size)] #lists of list


    def _hash(self,key):
        return key % self.size
    

    def insert(self, key, package):
        #Insert package with package id
        index = self._hash(key)
        #Check if key exist; if so, then replace
        for i, (k, p) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, package)
                return
        #If not found, apend to list
        self.table[index].append((key, package))

#get Package
    def get(self, key):
        #get package for key.
        index = self._hash(key)
        for k, p in self.table[index]:
            if k == key:
                return p
        return None