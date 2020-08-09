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
  # To keep it simple, once you replace one value,
  #  exit out of the function
  def replaceX(self, target, newValue):
      temp = self.head
      while temp:
          if temp.data == target:
              newNode = Node(newValue)
              newNode.next = temp.next
              if temp == self.head:
                  self.head = newNode
              else:
                  priorNode.next = newNode
              return
          priorNode = temp
          temp = temp.next




if __name__=='__main__':
  llist = LinkedList()

  llist.head = Node(1)
  second = Node(2)
  third = Node(3)

  llist.head.next = second
  second.next = third

  print("Before")
  llist.printLinkedList()
  # added this code
  llist.replaceX(1,3)
  print("After")
  llist.printLinkedList()
