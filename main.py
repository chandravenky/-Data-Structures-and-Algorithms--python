class Node():
    
    def __init__(self, data):    
        self.data= data
        self.next = None

class Stack():

    def __init__(self):
        
      self.top = None
      self.bottom = None
      self.length = 0

    def peek(self):
      return self.top.data

    def push(self, value):
      new_node = Node(value)

      if self.length ==0:
        self.top = new_node
        self.bottom = new_node
        self.length = self.length + 1
      
      else:
        
        new_node.next = self.top
        self.top = new_node
        self.length = self.length + 1

    def pop(self):

      if self.length == 0:
        return None
      
      pop_val = self.top.data
      self.top = self.top.next
      self.length = self.length -1
      return pop_val

    def printt(self):
      temp = self.top
      while temp != None:
        print(temp.data , end = ' -> ')
        temp = temp.next
      print()

myStack = Stack();
myStack.push('Google')
myStack.push('Discord')
myStack.push('Udemy')
myStack.printt()
peeked_val = myStack.peek()
print(peeked_val)
print(myStack.length)
myStack.pop()
myStack.printt()
print(myStack.length)