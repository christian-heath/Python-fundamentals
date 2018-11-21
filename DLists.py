class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
    def removeNode(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        runner = self.head
        while(runner != None):
            if runner.next.value == value:
                runner.next = runner.next.next
                return
            runner = runner.next
    def printAllValues(self, msg=""):
        runner = self.head
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg, "---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))
print("\n\n\n\n=================== START OF THE PROGRAM =================")
list = DoublyLinkedList(5)
list.addNode(6)
list.addNode(7)
list.addNode(8)
list.removeNode(6)
list.printAllValues("Attempt 1")