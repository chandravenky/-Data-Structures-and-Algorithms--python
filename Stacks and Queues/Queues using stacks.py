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
        """
        :rtype: int
        """
        

    def peek(self):
        """
        :rtype: int
        """
        

    def empty(self):
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push("Jerry")
obj.push("Sherry")
print(obj.first)
print(obj.last)

