class Hashtable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]
    
    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.Max
    '''
    def add_tohash(self, key, value):
        self.arr[self.get_hash(key)] = value
     '''   
    def access_value(self, key):
        return self.arr[self.get_hash(key)]

    def delete_element(self, key):
        self.arr[self.get_hash(key)] = None
        
    # collision handling in Hash tables
    
    def add_tohash_collision(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key, value)
                found = True
                break                
        if not found:
            self.arr[h].append((key, value))