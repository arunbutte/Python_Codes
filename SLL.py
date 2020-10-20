class Node:
    
    def __init__(self, data):
        self.data=data
        self.next=None
    
class linkedlist():
    
    def __init__(self):
        self.head=None
  
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next         
        
    def append(self, data):
        new_data=Node(data)
        
        if self.head is None:
            self.head=new_data
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            
            last_node.next=new_data
    
    def prepend(self, data):
        old_data=Node(data)
        
        old_data.next=self.head
        self.head=old_data
    
    def insert_after_node(self, previous_data, data):
        between_data=Node(data)
        
        between_data.next=previous_data.next
        previous_data.next= between_data   



lllist=linkedlist()
lllist.append("A")
lllist.append("Ab")
lllist.append("Abc")
lllist.append("Abcd")
lllist.append("Abcde")

lllist.insert_after_node(lllist.head.next, "E")
lllist.print_list()