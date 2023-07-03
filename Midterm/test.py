class Bracelet: #double linked list
	class Charm: #node
		def __init__(self, val):
			self.des = val
			self.prev_node = None
			self.next_node = None
			
	# def __init__(self, ls):
	# 	self.head = self.tail = None #create empty list
	# 	for ele in ls:
	# 		new_node = self.Charm(ele) #new node
	# 		if self.head is None: #empty list
	# 			self.head = self.tail = new_node
	# 		else: #list is not empty, insert to the tail
	# 			self.tail.next_node = new_node
	# 			new_node.prev_node = self.tail
	# 			self.tail = new_node
	def __init__(self, *args):
		self.head = self.tail = None #create empty list
		for ele in args:
			new_node = self.Charm(ele) #new node
			if self.head is None: #empty list
				self.head = self.tail = new_node
			else: #list is not empty, insert to the tail
				self.tail.next_node = new_node
				new_node.prev_node = self.tail
				self.tail = new_node

		
	def merge(self, b1):
		tp1  = b1.head
		tp2 = self.head
		while tp1 is not None and tp2 is not None:
			if tp2.next_node is None: #(list2 is shorter than list1 )
				tp2.next_node = tp1
				tp1.prev_node = tp2
				self.tail = b1.tail
				break
			else:
				cur = tp1
				tp1 = tp1.next_node
				cur.prev_node = tp2
				cur.next_node = tp2.next_node
				(tp2.next_node).prev_node = cur
				tp2.next_node = cur
				tp2 = tp2.next_node.next_node
		b1.head = b1.tail = None

	def printList(self):
		tp = self.head
		while tp is not None:
			print(tp.des, end = ' ')
			tp = tp.next_node


b1 = Bracelet(["Heart", "Star", "Diamond"])
b2 = Bracelet([1,2,3,4,5])

b1.merge(b2)

b1.printList()




    
             




    