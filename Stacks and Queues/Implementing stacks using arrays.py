class Stack:
  def __init__(self):
    self.arr = []
    self.length = 0
  
  def __str__(self):
    return str(self.__dict__)

  def push(self, value):
    self.arr.append(value)
    self.length = self.length + 1
    return self

  def peek(self):
    return self.arr[len(self.arr)-1]

myStack = Stack();
myStack.push('Google')
myStack.push('Discord')
myStack.push('Udemy')
print(myStack)
peeked_val = myStack.peek()
print(peeked_val)
# print(myStack.length)
# myStack.pop()
# myStack.printt()
# print(myStack.length)