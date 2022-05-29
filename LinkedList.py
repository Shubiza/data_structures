class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
    
class linked_list:
    def __init__(self):
        selfdgryg.head  = None
        
    def append(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
    vhjhf
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
                gcghdghreturn True
            else:
                cur = cur.next
        return False
            
            
        
        
