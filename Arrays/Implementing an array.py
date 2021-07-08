class myArray():
  def __init__(self):
    self.length = 0
    self.data = {}

  def __str__(self):
    return str(self.__dict__)

  def get(self, index):
    return self.data[index]

  def push(self, num):
    self.data[self.length]=num
    self.length = self.length + 1
    return self.data

  def pop(self):
    lastItem = self.data[self.length-1]
    del self.data[self.length-1]
    self.length = self.length-1
    return lastItem

  def delete(self, index):
    deleted_item = self.data[index]
    for i in range(index, self.length-1):
      self.data[i] = self.data[i+1]

    del self.data[self.length-1]
    self.length = self.length -1
    
    return deleted_item


arr = myArray()
print(arr)
arr.push(2)
print(arr)
arr.push(3)
print(arr)
print(arr.pop())
arr.push(4)
arr.push(5)
print(arr)
print(arr.delete(1))
print(arr)