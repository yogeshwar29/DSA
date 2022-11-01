class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def InsertBeginning(self, data):
        #Allocate the Node &
        #  Put in the data
        newNode = Node(data)
        # Make next of new Node as head
        newNode.next = self.head
        # Move the head to point to new Node
        self.head = newNode

    def insertmiddle(self, node, data):
        if node is None:
            print("node is not present")
            return

        #  Create new node &
        #  Put in the data
        newNode = Node(data)
        #  Make next of new Node as next of prev_node
        newNode.next = node.next
        # make next of prev_node as new_node
        node.next = newNode


    def insertend(self,data):
        # add data into newnode
        newNode = Node(data)
        # check if head is None
        if self.head is None:
            self.head = newNode
            return

        # itterate head
        itr = self.head
        # itr untill next is not None
        while itr.next != None:
            itr = itr.next
        # whn itr.next is None then add newNode
        itr.next = newNode

    def deleteStart(self):
        if self.head is None:
            print("Linked list is empty")
            return
        # make first elements next as head
        self.head = self.head.next

    def deleteNode(self, key):

        # Store head node
        curr = self.head
        prev = 0
        # If head node itself holds the key to be deleted
        if (curr is not None):
            if (curr.data == key):
                self.head = curr.next
                curr = None
                return
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (curr is not None):
            if curr.data == key:
                break
            prev = curr
            curr = curr.next
        # if key was not present in linked list
        if (curr == None):
            return
        # Unlink the node from linked list
        prev.next = curr.next
        curr = None




    def deleteEnd(self):
        if self.head is None:
            print("Link list is empty")
            return

        # itr in the list
        itr = self.head
        # itr untill next is not None
        while itr.next != None:
            itr = itr.next
            # itr.next.next = last node
            if itr.next.next is None:
                # itr.next = second last node
                itr.next = None

    def reverse(self, current):
        current = self.head
        prev = None
        while current != None:
            # store the next value
            next = current.next
            # shift the curr.next value to prev
            current.next = prev
            #update
            prev = current
            current = next
        #
        self.head.next = None
        self.head = prev




    def printlist(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next

l = LinkedList()
l.InsertBeginning(3)
l.InsertBeginning(5)
l.InsertBeginning(44)
l.insertend(11)
l.insertend(22)
l.deleteNode(3)
l.insertmiddle(l.head, 7)
#l.deleteEnd()
#l.deleteStart()
x = l.reverse(l.head)
l.printlist()

#
#
# while True:
#     print(x.data, end="<---")
#     x= x.next