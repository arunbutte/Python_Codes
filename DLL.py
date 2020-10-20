class DNode:
    
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
        
class Doublylinkedlist():
    
    def __init__(self):
        self.head=None
        
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next 
    
    def append(self, data):
        
        append_data=DNode(data)
        
        if self.head is None:
            self.head=append_data
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=append_data
            append_data.next=None
            append_data.prev=last_node
            
    def prepend(self, data):
            
        prepend_data=DNode(data)
            
        if self.head is None:
            self.head=prepend_data
            prepend_data.prev=None
        else:
            '''
            first_element=self.head
            self.head=prepend_data
            prepend_data.next=first_element
            prepend_data.prev=None
            '''
            self.head.prev=prepend_data
            prepend_data.next=self.head
            self.head=prepend_data
            prepend_data.prev=None
            #both logics are true
        
    def delete(self, key):
        
        cur_node = self.head
        
        while cur_node:
            #case 1:Only one element in the list
            if cur_node == self.head and key == cur_node.data:
                if not cur_node.next:
                    cur_node=None
                    self.head=None
                    return
                
                #case 2: more then one element and want to remove the head element
                else:
                    next_node=cur_node.next
                    cur_node.next=None
                    cur_node=None
                    next_node.prev=None
                    self.head=next_node
                    return
            
            elif cur_node.data == key :
                #case 3: delete the in between node, nearrest to head node
                if cur_node.next:
                    next_node=cur_node.next
                    prev_node=cur_node.prev
                    next_node.prev=prev_node
                    prev_node.next=next_node
                    cur_node.next=None
                    cur_node.prev=None
                    cur_node=None
                    return
                
                else:
                    prv=cur_node.prev
                    prv.next=None
                    cur_node.prev=None
                    cur_node=None
                    return
                
            cur_node=cur_node.next
            

    def add_after_node(self, key, data):
        
        afternode=DNode(data)
        cur_node=self.head
        
        while cur_node:
            if cur_node.next is None and cur_node.data == key:
                
                self.append(data)
                
            elif cur_node.data == key:
                
                next_node=cur_node.next
                afternode.prev=cur_node
                afternode.next=next_node
                cur_node.next=afternode
                next_node.prev=afternode
            
            cur_node=cur_node.next


    def add_before_node(self, key, data):

            beforenode=DNode(data)
            cur_node=self.head

            while cur_node:
                if cur_node.next is None and cur_node.data == key:

                    self.append(data)

                elif cur_node.data == key:

                    prev_node=cur_node.prev
                    beforenode.next=cur_node
                    beforenode.prev=prev_node
                    cur_node.prev=beforenode
                    prev_node.next=beforenode

                cur_node=cur_node.next
        
                
                    
            
#test cases

Dll=Doublylinkedlist()
Dll.prepend(0)
Dll.append(1)
Dll.append(2)
Dll.append(3)
#Dll.append(4)
#
#Dll.prepend(-1)
#Dll.prepend(-2)
#Dll.delete(3)

Dll.add_after_node(2,2.5)
Dll.add_before_node(2.5,2.1)

Dll.print_list()