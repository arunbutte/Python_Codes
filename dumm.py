######Binary Tree#######
"""
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



"""

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