class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None

    
    def enqueue(self,data):
        if self.head == None:
            self.data = Node(data)
        node = Node(data)
        node.next = self.head
        self.head = node
        

    def display(self):
        current = self.head
        while current:
            print(current.data,end = " ")
            current = current.next
        
    
    def dequeue(self):
        current = self.head
        if self.is_empty() == True:
            return "No items to delete"
        current.data = None
        current = current.next

    def is_empty(self):
        if self.data is None:
            return True
        
    def length(self):
        c = 0
        current = self.head
        while current:
            c+=1
            current = current.next
        return '\n',c

    def peek(self):
        print(self.head.data)

    def max(self):
        c = self.head.data
        while self.head:
            if self.head.data > c:
                c = self.head.data
            self.head = self.head.next
        return c
    
    def min(self):
        c = self.head.data
        if self.head is None:
            print('The queue is empty ')
        while self.head:
            if self.head.data < c:
                c = self.head.data
            self.head = self.head.next
        return c

my = Queue()
my.enqueue(23)
my.enqueue(3)
my.enqueue(100)
my.enqueue(34)
my.peek()
my.length()
my.is_empty()
my.dequeue()
my.display()