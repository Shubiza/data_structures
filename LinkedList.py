class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
    
class linked_list:
    def __init__(self):
        self.head  = None
        
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def len(self):
        total = 0
        cur = self.head
        while cur.next!= None:
            total += 1
            cur = cur.next
        return total
        
    def display(self):
        list = []
        cur = self.head
        while cur.next != None:
            list.append(cur.data)
        return list
        
    L1 = linked_list()
    L1.append(1)
    L1.append(2)
    L1.append(3)
    L1.append(4)
    L1.append(5)
    print(L1.len())
    print(L1.display())