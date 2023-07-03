class Node:
    def __init__(self, data, set_list, next_node, prev_node):
        #setting the data
        self.data = data
        self.set_list = set_list
        self.next_node = next_node
        self.prev_node = prev_node
    # a Node has 4 members: data, next_node, prev_node, set_list

    def get_data(self):
        #return the data stored in node
        # return self.set_list # mistake
        return self.data

    def get_next(self):
        #returning the next node in SetList
        return self.next_node

    def get_previous(self):
            #returning the previous node in SetList
        return self.prev_node

    def get_set(self): #self is the same as 'this' keyword in C++ --> refer to the current Object that calls this function
        #function returns reference to the SetList
        # if self is None or self == "":
        #     return None
        # return self.data #mistake
        return self.set_list
    
    #addition methods
    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def set_set_list(self, set_list):
        self.set_list = set_list

class SetList:
    def __init__(self):
        #setList becomes empty when initalized
        self.head = None
        self.tail = None
    #setList has 2 members: Node head and tail

    def get_front(self):
        #This function returns a reference to the first node in the list --> header of List --> head reference
        return self.head 

    def get_back(self):
        #to return the last node
        return self.tail

    def make_set(self, data):
        #This function adds the first value to the SetList object if the list is empty and returns a reference to newly created Node.
        #If the list is not empty, function does nothing and returns None. 
        # if the list is empty --> create a new Node with passed data and add that Node to the setLilst
        # else: does nothing and return None
        if self.head is None: # List is empty
            #constructor of Node: (data, set_list, next_node, prev_node)
            # new_node has: next = prev = None, data = passed data, set_list = self = current SetList that contains created new_node
            new_node = Node(data, self, None, None)
            self.head = new_node
            self.tail = new_node
            # new_node
            return new_node
        else: 
            return None

    def find_data(self, data):
        #check and return data
        current = self.head 
        # current is a Node reference
        # current:Node
        # starting with current reference that refers to the head of List
        while current is not None: # condition: the list still has none-visited Node --> continue while loop
            if current.data == data:
                return current
            current = current.next_node
        return None #not found

    def representative_node(self):
       #check if empty if not return the node
        # if self.head is None:
        #     return None
        # else:
        #     return self.head
        return self.head

    def representative(self):
        #calls the representative_node
        representative_node = self.representative_node()
        if representative_node is None:
            return None
        else:
            return representative_node.get_data()

    def union_set(self, other_set):
        # count = 0

        # current = other_set.head
        # while current is not None:
        #     current.set_list = self
        #     current = current.next_node
        #     count += 1

        # if other_set.head is not None:
        #     self.tail.next_node = other_set.head
        #     other_set.head.prev_node = self.tail
        #     self.tail = other_set.tail

        # other_set.head = None
        # other_set.tail = None

        # return count
        count = 0
        current = other_set.head # current:Node
        # find_data(data) will return None if not found the data in List
        while current is not None:
            if self.find_data(current.get_data()) is None: #the currentNode is not exsist in this SetList
                #add current to the tail of list
                # move current from other_set to current set --> must re-set set_list of currentNode
                # check current List is empty or not
                temp = current
                current = current.next_node
                if self.head is None:
                    self.head = self.tail = temp
                    temp.set_next_node(None)
                    temp.set_prev_node(None)
                    temp.set_set_list(self)
                    
                else:
                    self.tail.set_next_node(temp)
                    temp.set_next_node(None)
                    self.tail.set_prev_node(self.tail)
                    self.tail = temp
                    temp.set_prev_node(None)
                    temp.set_set_list(self)
                count += 1
            else:
                current = current.next_node
        
        other_set.head = None
        other_set.tail = None
        return count

    def __len__(self):
        #the number of items in the Set List
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next_node
        return count
