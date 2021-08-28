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
