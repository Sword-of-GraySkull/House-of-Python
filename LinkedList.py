# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:46:11 2020

@author: Venni
"""

# Linked List

# Class Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, val):
        self.data = val
        
    def setNext(self, val):
        self.next = val
        
class LinkedList():
    """
    Creates a Linked List
    
    Attributes:
        add(item):
            adds the given item at the beginning of the Linked list
            
        isEmpty():
            returns True if the List is Empty
            
        size():
            returns the Size of the Linked List
            
        remove(item):
            removes the item from the List if found
            if not found raises ValueError
            
        search(item):
            searches for the given item 
            returns True if Found
            
        insert(item, position):
            adds the given item at the given position
            raises IndexError if index exceeds the size of the List
            
        pop(item, position = None):
            removes and returns the Given item if found
            Position = 0 by default
            
        index(item):
            return the index where the item if Found
            
        append(item):
            adds the item at the end of the Linked List
            
        printList():
            prints the Linked List
    """
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count
    
    def add(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node
        
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext)
        else:
            raise ValueError
            print('Value Not Found')
    
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True 
            else:
                current = current.getNext()
        return found
    
    def insert(self, position, item):
        if position > self.size() - 1:
            raise IndexError
            print('Index out of Bounds')
        current = self.head
        previous = None
        pos = 0
        if position is 0:
            self.add(item)
        else:
            new_node = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.getNext()
            previous.setNext(new_node)
            new_node.setNext(current)
            
    def pop(self, position):
        if position > self.size() - 1:
            raise IndexError
            print('Index out of Bounds')
        current = self.head
        if position is None:
            ret = current.getData()
            self.head = current.getNext()
        else:
            pos = 0
            previous = None
            while pos < position:
                pos += 1
                previous = current 
                current = current.getNext()
            ret = current.getData()
            previous.setNext(current.getNext())
        print(ret)
        return ret

    def index(self, item):
        current = self.head
        found = False
        pos = 0
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                pos += 1
                current = current.getNext()
        if found:
            pass
        else:
            raise ValueError
            print('Value not Found')
        return pos
    
    def append(self, item):
        current = self.head
        previous = None
        pos = 0
        length = self.size()
        while pos < length:
            pos += 1
            previous = current
            current = current.getNext()
        new_node = Node(item)
        if previous is None:
            new_node.setNext(current)
            self.head = new_node
        else:
            previous.setNext(new_node)
    
    def printList(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()
            
            
            