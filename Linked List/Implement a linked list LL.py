class Node():
    
    def __init__(self, data):    
        self.data= data
        self.next = None
    

class LinkedList():

    def __init__(self):
      self.head = None
      self.tail = None
    
    def append(self, data):
        
        if self.head == None:
            self.head = Node(data)
            self.tail = Node(data)
            self.length = 1
        
        else:
            self.head.next = Node(data)
            self.tail = Node(data)
            self.length = self.length +1
            
    def print_list(self):
        temp = self.head
        i = 0
        while i < self.length:
            print(temp.data, end='-->')
            temp = temp.next
            i += 1
        print()

myLL = LinkedList()
print(myLL)
myLL.append(10)
myLL.print_list()
myLL.append(20)
myLL.print_list()
