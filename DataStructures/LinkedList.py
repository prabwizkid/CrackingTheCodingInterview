class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = node

    def insertStart(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAt(self, data, index):
        node = Node(data)
        if index == 0:
            self.insertStart(data)
        else:
            n = self.head
            for i in range(index):
                n = n.next
            node.next = n.next
            n.next = node

    def show(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def getIndex(self, data):
        index = 0
        node = self.head
        while node:
            if node.data == data:
                break
            else:
                node = node.next
                index += 1

        return index

    def isNode(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            else:
                node = node.next
        return False

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            n = self.head
            for i in range(index-1):
                n = n.next
            n1 = n.next
            n.next = n1.next


if __name__ == "__main__":

    ll = LinkedList()
    ll.insertEnd(1)
    ll.insertStart(3)
    ll.insertEnd(5)
    ll.insertAt(8, 1)
    print(ll.isNode(3))
    print(ll.getIndex(8))
    print("--------")
    ll.show()
    print("--------")
    ll.delete(2)
    ll.show()