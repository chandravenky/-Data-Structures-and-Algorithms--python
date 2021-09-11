# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:42:57 2021

@author: venkatesh.chandra
"""


class Node():
    
    def __init__(self, data):    
        self.data= data
        self.next = None
        self.prev = None
    

class DoublyLinkedList():

    def __init__(self, value):
        
      self.head = Node(value)
      self.tail = self.head
      self.length = 1
      
    def __str__(self):
        return '{self.head.next.data} {self.tail.prev.data}'.format(self=self)
    
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        new_node.prev = self.tail
        self.length = self.length +1
    
    def prepend(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
        self.length = self.length +1
        
    def insert(self, index, value):

        if index ==0:
          self.prepend(value)
          return None

        elif index >=self.length-1:
          self.append(value)
          return None

        currentNode = self.head
        for i in range(0, index-1):
          currentNode = currentNode.next

        newNode = Node(value)
        nextNode = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode
        newNode.next = nextNode 
        nextNode.prev = currentNode
        self.length = self.length +1

    def remove(self, index):

        if index==0:
          self.head = self.head.next
          self.length = self.length -1
          return None

        currentNode = self.head
        for i in range(0, index-1):

          currentNode = currentNode.next

        deleteNode = currentNode.next
        nextNode = deleteNode.next
        currentNode.next = nextNode
        self.length = self.length -1


    def print1(self):

        temp = self.head

        while temp != None:

            print(temp.data, end = ' ')

            temp = temp.next

        print()

        print("Length = " + str(self.length))



myLL = DoublyLinkedList(10)
myLL.append(15)
myLL.print1()
myLL.append(20)
myLL.print1()
myLL.prepend(5)
myLL.print1()
myLL.insert(2,12)
myLL.print1()

# myLL.prepend(7)
# myLL.print1()
# myLL.append(10)
# myLL.print1()
# myLL.append(20)
# myLL.print1()
# myLL.prepend(5)
# myLL.print1()
# myLL.append(25)
# myLL.print1()
# myLL.insert(3,12)
# myLL.print1()
# myLL.insert(0,1)
# myLL.print1()
# myLL.remove(3)
# myLL.print1()
# myLL.remove(0)
# myLL.print1()
# print(myLL.head.data)