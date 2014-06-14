class Node:
    def __init__(self,item,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return repr(self.item)
class BinaryTree:
    def __init__(self,item=None,left=None,right=None):
        self.root = Node(item)
        self.root.left = left
        self.root.right = right

    def add_right(self,item):
        if self.root == None:
            self.root = Node(item)
        curr = self.root
        while curr.right != None:
            curr = curr.right
        new_node = Node(item)
        curr.right = new_node
    
    def add_left(self, item):
        if self.root == None:
            self.root = Node(item)
        curr = self.root
        while curr.left != None:
            curr = curr.left
        new_node = Node(item)
        curr.left = new_node
        
    def contains(self,val):
        return self.__contains(val,self.root)
        

    def __contains(self,val,curr):
        if curr.item == val: return True
        else:
            if curr.left: 
                return self.__contains(val,curr.left)
            if curr.right: 
                return self.__contains(val,curr.right)
            else: return False
            

    def pretty_print(self):
        self.__pretty_print(self.root)
        
    def __prety_print(self,node):
        if node == None:
            return
        self.__pretty_print(node.left)
        print node.item
        self.__pretty_print(node.right)

