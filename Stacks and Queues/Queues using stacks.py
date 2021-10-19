class MyQueue(object):

    def __init__(self):
      self.first=[]
      self.last=[]
        

    def push(self, value):
        length = len(self.first)
        for i in range(0, length):
          self.last.append(self.first.pop())
        
        self.last.append(value)
        

    def pop(self):
        if len(self.first)>0:
          return self.first.pop()
        length = len(self.last)
        for i in range(0, length):
          self.first.append(self.last.pop())
        
        return self.first.pop()

    def peek(self):
        if len(self.last)>0:
          return self.last[0]
        return self.first[len(self.first)-1]

    def empty(self):
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push("Jerry")
print(obj.first)
print(obj.last)
obj.push("Sherry")
print(f"peek value => {obj.peek()}")
print(obj.first)
print(obj.last)
print(obj.pop())
print(obj.first)
print(obj.last)
obj.push("Limca")
print(f"peek value => {obj.peek()}")
print(obj.first)
print(obj.last)
print(obj.pop())
print(obj.first)
print(obj.last)
print(f"peek value => {obj.peek()}")

