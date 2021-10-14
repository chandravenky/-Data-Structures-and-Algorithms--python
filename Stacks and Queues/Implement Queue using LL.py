class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0 

  def enqueue(self, value):
    new_node = Node(value)
    if self.length ==0:
      self.first = new_node
      self.last = self.first
      self.length = self.length + 1

    else:
      self.last.next = new_node
      self.last = new_node
      self.length = self.length + 1

  def peek(self):
    return self.first.value

  def dequeue(self):
    dequeued_val = self.first
    self.first = self.first.next
    self.length = self.length - 1

    return dequeued_val
    
  def printt(self):
    temp = self.first
    while temp != None:
      print(temp.value , end = '->')
      temp = temp.next
    print()
    print(self.length)

myQueue = Queue();
myQueue.enqueue('Google')
myQueue.enqueue('Discord')
myQueue.enqueue('Udemy')
myQueue.printt()
# x = myQueue.peek()
# print(x)
myQueue.dequeue()
myQueue.printt()
myQueue.dequeue()
myQueue.printt()