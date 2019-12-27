class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
	def push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node
	def insertAfter(self,prev_node,new_data):
		new_node=Node(new_data)
		if prev_node is None:
			print("The given node should be in LinkeddList")
			return
		new_node.next=prev_node.next
		prev_node.next=new_node

	def append(self,new_data):
		new_node=Node(new_data)
		if self.head is None:
			self.head=new_node
			return
		last=self.head
		while(last.next):
			last=last.next
		last.next=new_node
	def PrintList(self):
		temp=self.head
		while(temp):
			print(temp.data)
			temp=temp.next

if __name__=='__main__':
	llist=LinkedList()
	llist.append(6)
	print('Created linked list is:')
	llist.PrintList()
	llist.push(7);
	print('Created linked list is:')
	llist.PrintList()
	llist.push(1);
	print('Created linked list is:')
	llist.PrintList()
	llist.append(4)
	print('Created linked list is:')
	llist.PrintList()
	llist.insertAfter(llist.head.next, 8)
	print('Created linked list is:')
	llist.PrintList()
