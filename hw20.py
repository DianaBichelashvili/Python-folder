
class Treenode:
    def __init__(self, key):
        self.root= None



class BinaryTree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

def print_leaf(self,node, leaf):
    if node is None:
        return
    
    if node.left is None and node.right is None:
        print(node.key)  
    else:
        if node.left is not None:
            print_leaf(node.left)
        if node.right is not None:
            print_leaf(node.right)




def count_edges(node):
    if node is None:
        return 
    left_edges = count_edges(node.left)

    right_edges = count_edges(node.right)
    
    return left_edges + right_edges 




