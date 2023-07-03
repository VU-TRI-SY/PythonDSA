class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#linked list
class SingleLinkedList:
    def __init__(self): #constructor to create empty list
        self.head = None #head: reference of type Node

    def isEmpty(self):
        return self.head is None
    
    def size(self):
        ct = 0
        cur = self.head
        while cur is not None:
            ct += 1
            cur = cur.next

        return ct

    def insert(self, data, position=-1): #call function insert(dat) with passed dat --> create new node that has data = dat and insert to list
        #if position = -1 --> insert to tail
        #insert(10) --> position = -1 --> insert to tail
        #insert(10, 2) --> insert new node to become index 2 in list
        if position == -1:
            if self.isEmpty():
                self.head = Node(data) #create single node
            else:
                cur = self.head
                while cur.next is not None:
                    cur = cur.next
                #after running while, cur will refer to the Node that has next pointer = null --> cur is refering to tail of list
                cur.next = Node(data) #create single node #link newNode to the list
        else:
            if self.isEmpty():
                self.head = Node(data) #create single node
            else:
                if position == 0:
                    newNode = Node(data)
                    newNode.next = self.head
                    self.head = newNode
                elif position >= self.size():
                    self.insert(data)
                elif position > 0:
                    index = 0
                    cur = self.head
                    #find the Node that has index = position-1 and insert newNode after that Node
                    while index != position-1:
                        index += 1
                        cur = cur.next
                    newNode = Node(data)
                    newNode.next = cur.next
                    cur.next = newNode

    def remove(self, data=None, index=-1):
        if self.isEmpty():
            return
        if data is None:
            if index == -1:
                if self.head.next is None: #list has only 1 Node
                    self.head = None
                else: #list has >= 2 Nodes
                    cur = self.head
                    while cur.next.next is not None:
                        cur = cur.next
                    cur.next = None
            elif 0 <= index < self.size(): #index is valid
                if index == 0:
                    self.head = self.head.next
                else:
                    #find the node that is right next deleted node
                    id = 0
                    cur = self.head
                    while id != index-1:
                        cur = cur.next
                        id += 1
                    
                    # if cur.next.next is None: #remove tail
                    #     cur.next = None
                    # else:
                    #     cur.next = cur.next.next
                    cur.next = cur.next.next
        else:
            prev = None
            cur = self.head
            #cur refers to the deleted node, prev refers to node that is right next to deleted node 
            while cur is not None:
                if cur.data == data:
                    if prev is None:
                        self.head = self.head.next
                    else:
                        prev.next = prev.next.next
                    
                    return
                else:
                    prev = cur
                    cur = cur.next


    def reverse(self):
        if self.head is None or self.head.next is None:
            return
        prev = None
        cur = self.head
        while cur is not None:
            tp = cur
            cur = cur.next
            tp.next = prev
            prev = tp
        #after running while --> cur = None and prev will refer to the last node of old list
        self.head = prev

    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end = " ")
            cur = cur.next
        print()

ll = SingleLinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.display()
ll.reverse()
ll.display()

