class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
    
class Linked_list:
    def __init__(self):
        self.head  = None
        
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
    
    def len(self):
        total = 0
        cur = self.head
        while cur != None:
            total += 1
            cur = cur.next
        return total
        
    def display(self):
        list_ = []
        cur = self.head
        while cur != None:
            list_.append(cur.data)
            cur = cur.next
        return list_
        
    def search(self,val):
        cur = self.head
        while cur != None:
            if cur.data == val:
                return True
            else:
                cur = cur.next
        return False
            
    def remove_from_last(self):
        cur = self.head
        if self.head == None:
            return None
        else:
            while cur.next.next !=  None:
                cur = cur.next
            pop = cur.next
            cur.next = None
            
    def return_last_node(self):
        cur = self.head             
        while cur.next != None:
            cur = cur.next
        return cur.data

            
        
        
class Stack:
    def __init__(self):
        self.stack = Linked_list()

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.remove_from_last()

    def top(self):
        return self.stack.return_last_node()

    def display(self):
        print self.stack.display()

    
stack1 = Stack()
stack1.push(2)
stack1.push(34)
stack1.push(78)
stack1.push(4)
stack1.push(3)
stack1.display()
stack1.pop()
stack1.display()

