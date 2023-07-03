from a1_partb import SetList

class DisjointSet:
    def __init__(self):
        self.m_dict = dict()
    
    def make_set(self,element):
        if element in self.m_dict:
            return False
        else:
            sl = SetList()
            node = sl.make_set(element)
            self.m_dict[element] = node # add key-value pair to dictionary
            return True

    def find_set(self, element):
        # Function returns the representative of the set containining element
        if element in self.m_dict:
            #key-value: element-Node
            # found_node = self.m_dict[element] #node that contains element
            # return found_node.get_set() #return SetList reference that contains found_node
            return self.m_dict[element].get_set().representative()
        else:
            return None
    
    def get_num_sets(self):
        # Function returns the number of disjoint sets
        ls = list()
        for key, val in self.m_dict.items():
            if val.get_set() not in ls: #if the SetList reference is not in the list --> add to list
                ls.append(val.get_set())
        
        return len(ls)
    
    def __len__(self):
        return len(self.m_dict) #return the number of key-value pairs in dictionary
    
    def get_set_size(self, element):
        if element in self.m_dict:
            return len(self.m_dict[element].get_set())
        # self.m_dict[element] --> return the Node that contain the element
        # .get_set() --> return the reference (SetList) containe that Node
        # len(self.m_dict[element].get_set()): in SetList, it has __len__ method --> len(SetList) will return the lenght of that SetList
        else:
            return 0
        
    def union_set(self, element1, element2):
        if element1 not in self.m_dict or element2 not in self.m_dict:
            return False
        
        s1 = self.m_dict[element1].get_set()
        s2 = self.m_dict[element2].get_set()

        if s1 == s2:
            return False
        else:
            s1.union_set(s2)
            return True
                