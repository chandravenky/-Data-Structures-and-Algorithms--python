# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:42:57 2021

@author: venkatesh.chandra
"""


class Node():
    
    def __init__(self, data):    
        self.data= data
        self.next = None
    

class LinkedList():

    def __init__(self, value):
        
      self.head = Node(value)
      self.tail = self.head
      self.length = 1
      
    def __str__(self):
        return str(self.__dict__)
    
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.length = self.length +1
    
    def prepend(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length = self.length +1
        
    def insert(self, index, value):

        currentNode = self.head
        for i in range(0, index):
          print(i)
          currentNode = currentNode.next

        newNode = Node(value)
        nextNode = currentNode.next
        currentNode.next = newNode
        newNode.next = nextNode  

    def print1(self):

        temp = self.head

        while temp != None:

            print(temp.data, end = ' ')

            temp = temp.next

        print()

        print("Length = " + str(self.length))

myLL = LinkedList(10)
myLL.prepend(7)
myLL.print1()
myLL.append(10)
myLL.print1()
myLL.append(20)
myLL.print1()
myLL.prepend(5)
myLL.print1()
myLL.append(25)
myLL.print1()
myLL.insert(3,12)
myLL.print1()
