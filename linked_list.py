# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def list_print(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
        print("\n")
    
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
        
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        currentval = self.headval
        if currentval is None:
            self.headval = NewNode
            return
        while currentval.nextval is not None:
            currentval = currentval.nextval
        currentval.nextval = NewNode
    
    def InBetween(self, fromnode, newdata):
        if fromnode is None:
            print("No such node exists")
            return
        NewNode = Node(newdata)
        NewNode.nextval = fromnode.nextval
        fromnode.nextval = NewNode
    
    def RemoveNode(self, RemoveKey):
        Head = self.headval
        if Head is None:
            return
        if Head.dataval == RemoveKey:
            self.headval = Head.nextval
            Head = None
            return
        while Head.nextval is not None:
            if Head.nextval.dataval == RemoveKey:
                Head.nextval = Head.nextval.nextval
                return
            Head = Head.nextval
        

l1 = SLinkedList()

head = Node("Mon")
l1.headval = head

e2 = Node("Tue")

e3 = Node("Wed")

head.nextval = e2
e2.nextval = e3

l1.list_print()

l1.AtBeginning("Sun")

l1.list_print()

l2 = SLinkedList()

l2.AtEnd("Thu")
l2.list_print()

l1.InBetween(l1.headval.nextval, "Fri")

l1.list_print()

l1.RemoveNode("Fri")
l1.list_print()