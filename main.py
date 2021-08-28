class Hashtable:
    
    def __init__(self, size):
        self.data = [None]*size
 
    def __str__(self):
        return str(self.__dict__)
  
    def _hash(self, key):
        hash = 0
        i = 0
        while i < len(key):
          hash = (hash + ord(key[i]) * i) % len(self.data)
          i += 1
        return hash
    
    def set(self, key, value):

        address = self._hash(key)
        
        if not self.data[address]:
            
            self.data[address] = []
        
        self.data[address].append([key, value])

        return self.data

    def get(self, key):
    
        address = self._hash(key)

        if self.data[address]:
            
            for  [stored_key,value] in self.data[address]:
                
                if stored_key == key:
                    
                    return value
            
        return None


    def  keys(self):
      
        keys_result = []
        
        for item in self.data:
            
            if item:
                
                for key,_ in item:
                    
                
                    keys_result.append(key)
      
        return keys_result


    def remove(self, key):
        
        address = self._hash(key)
        
        if self.data[address]:
        
            for i in range(0, len(self.data[address])):
                
                if self.data[address][i][0] == key:
                    
                    self.data[address].pop(i)
                    
            if self.data[address] == []:

                self.data[address] = None
                        
        return None
	



'''
h = Hashtable(50)
h.set('grapes', 10000)
h.set('grapes', 20000)
print(h.get('grapes'))
print(h.keys())
'''

k = Hashtable(50)
k.set('grapes', 10000)
k.set('apples', 20000)
print(k)
print(k.get('grapes'))
print(k.get('apples'))
print(k.keys())
print(k.remove('apples'))
print(k)


