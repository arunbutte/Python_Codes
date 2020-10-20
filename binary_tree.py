######Binary Tree#######

class stack(object):
	def __init__(self):
		self.items = []
	
	def push(self, item):
		return self.items.append(item)
	
	def pop(self):
		if not self.is_empty():
			return self.items.pop()
	
	def is_empty(self):
		return len(self.items) == 0
	
	def peek(self):
		if not self.is_empty():
			return self.items[-1]
			
	def __len__(self):
		return self.size()
		
	def size(self):
		return len(self.items)		



class queue(object):
    def __init__(self):
        self.items = []
    
    def insert_Q(self, item):
        self.items.insert(0, item)  #inserting at 0-th position
        
    def is_empty(self):
        return len(self.items) == 0
    
    def de_Q(self):
        if not self.is_empty():
            return self.items.pop() # removes the first element from the items
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
		
		
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class binarytree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def print_root(self, traversal_type):
        if traversal_type == "pre_order":
            return self.pre_order(tree.root, "")
        elif traversal_type == "in_order":
            return self.in_order(tree.root, "")
        elif traversal_type == "post_order":
            return self.post_order(tree.root, "")
        elif traversal_type == "level_order":
            return self.level_order(tree.root)
        elif traversal_type == "reverse_order":
            return self.reverse_order(tree.root)
        else:
            return print ("invalid", traversal_type)
        
    def pre_order(self, start, traversal):        
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal

    def in_order(self, start, traversal):        
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += (str(start.value) + "-")            
            traversal = self.in_order(start.right, traversal)
        return traversal

    def post_order(self, start, traversal):        
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal = self.in_order(start.right, traversal)
            traversal += (str(start.value) + "-") 

        return traversal

    def level_order(self, start):
        if start is None:
            return    
        
        q = queue()
        q.insert_Q(start)
        
        traversal = ""
        while len(q) > 0:    # till the items are present
            
            traversal += str(q.peek()) + "-"
            node = q.de_Q()
            
            if node.left:
                q.insert_Q(node.left)
                
            if node.right:
                q.insert_Q(node.right)
                
        return traversal 
		
	
    def reverse_order(self, start):
        if start is None:
            return    
        
        q = queue()
        q.insert_Q(start)
        s = stack()
    	
        traversal = ""
    	
        while len(q) > 0:
    	    node = q.de_Q()
    	    s.push(node)
    		
    	    if node.right:
    		    q.insert_Q(node.right)
    	    if node.left:
    	        q.insert_Q(node.left)
    	
        while len(s) > 0:
    	    node = s.pop()
    	    traversal += str(node.value) + "-"		
        return traversal
    		

    def height(self, node):
	    if node is None:
		    return -1
	    else:
		    left_h = self.height(node.left)
		    right_h = self.height(node.right)
		
	    return 1 + max(left_h, right_h)
	
    def size(self):
        if self.root is None:
            return 0
        else:
            s = stack()
            s.push(self.root)
            size = 1
            while s:        #till the elements are present in stack()
                node = s.pop()
                if node.left:
                    size += 1
                    s.push(node.left)
                if node.right:
                    size += 1
                    s.push(node.right)
            return size

    def size_node(self, node):
	    if node is None:
		    return 0
	    else:
		    return 1 + self.size_node(node.left) + self.size_node(node.right)
					
				

##test cases

tree = binarytree(1)

tree.root.right = Node(3)
tree.root.left = Node(2)

tree.root.right.right = Node(7)
tree.root.right.left = Node(6)

tree.root.left.right = Node(5)
tree.root.left.left = Node(4)

#tree.root.right.right.right = Node(8)
#tree.root.right.right.left = Node(9)

#tree.root.right.right.right = Node(8)

print(tree.print_root("pre_order"))
print(tree.print_root("in_order"))
print(tree.print_root("post_order"))
print(tree.print_root("level_order"))
print(tree.print_root("reverse_order"))

print(tree.height(tree.root))

print(tree.size())

print(tree.size_node(tree.root))
