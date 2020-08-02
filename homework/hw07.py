class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printLinkedList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

# TODO
  def find(self, key):
      temp = self.head
      while temp:
          if temp.data == key:
              return key
          temp = temp.next
      return "None"



if __name__=='__main__':
  llist = LinkedList()

  llist.head = Node(1)
  second = Node(2)
  third = Node(3)

  llist.head.next = second
  second.next = third

  #llist.printLinkedList()

  # find method
  print(llist.find(2))
  print(llist.find(5))
  #def find()
