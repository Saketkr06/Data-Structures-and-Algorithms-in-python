class Node:
    def __int__(self,value=None):
        self.value=value
        self.next=next
class SLinkedList:
    def __int__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    #insert in linked list
    def insertSLL(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location == 0:
                newNode.next=self.head
                self.head=newNode
            elif location==1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index <location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode

singlyLinkedList=SLinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(0,0)
singlyLinkedList.insertSLL(0,4)


from random import randint
class Node:
    def __int__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self,values=None):
        self.head=None
        self.tail=None

    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next
    def __str__(self):
        values=[str(x.value) for x in self]
        return  "->".join(values)
    def __len__(self):
        result=0
        node=self.head
        while node:
            result +=1
            node=node.next
        return result
    def add(self,value):
        if self.head is None:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next

        return self.tail

    def generate(self,n,min,max):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(min,max))

        return self


customLL=LinkedList()
customLL.generate(10,0,99)
print(customLL)
















