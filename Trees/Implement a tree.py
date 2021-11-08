# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:00:37 2021

@author: venkatesh.chandra
"""


class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
  

class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self, data):
    new_node = Node(data)

    if self.root == None:
      self.root = new_node
      return
    
    else:
      current_node = self.root
      
      while True:
        if data < current_node.data:
  
          if not current_node.left:
  
            current_node.left = new_node
            return
  
          else:
            current_node = current_node.left
  
        elif data > current_node.data:
  
          if not current_node.right:
  
            current_node.right = new_node
            return
            
          else:
            current_node = current_node.right

  def lookup(self, value):
      
      if not self.root:
          return False
      
      current_node = self.root
      while current_node:
          
          if value <current_node.data:
              current_node= current_node.left
          
          elif value >current_node.data:
              current_node= current_node.right
          elif current_node.data == value:
              return current_node
          
      return False

  def print_tree(self):
    if self.root != None:
      self.printt(self.root)
      
  def printt(self,curr_node):
    if curr_node != None:
      self.printt(curr_node.left)
      print(str(curr_node.data))
      self.printt(curr_node.right)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
bst.print_tree()
x = bst.lookup(5)
print(x)
bst.printt(x)