import numpy as np

def main():
    tree1 = Tree_node()
    tree1.value = 250
    tree1.ID = 360
    tree1.create_tree(tree1, depth=2)
    tree1.print_tree(tree1)
    print(tree1.is_binary_search_tree(tree1))
    
    tree1 = Tree_node_binary_search()
    tree1.value = 250
    tree1.ID = 360
    tree1.create_binary_search_tree(tree1, depth=2)
    tree1.print_tree(tree1)
    print(tree1.is_binary_search_tree(tree1))

class Tree_node(object):
    def __init__(self, value=None, left=None, right=None, ID=None):
        self.left = left
        self.right = right
        self.value = value
        self.ID = ID
        self.all_IDs = []
        self.all_nodes = []
        
    def set_left(self, node):
        self.left = node
        
    def set_right(self, node):
        self.right = node
        
    def print_tree(self, root):
        if root is None:
            return
        print("ID: {}, value: {}".format(root.ID, root.value))
        self.print_tree(root.left)
        self.print_tree(root.right)
        
    def add_left_subtree(self, root, depth_sub_tree):
        while root.left is not None:
            root = root.left
        self.create_tree(root, depth_sub_tree)
        
    def get_IDs(self, root):
        if root is None:
            return
        self.all_IDs.append(root.ID)
        self.get_IDs(root.left)
        self.get_IDs(root.right)
        return self.all_IDs
    
    def get_nodes(self, root):
        if root is None:
            return
        self.all_nodes.append(root)
        self.get_nodes(root.left)
        self.get_nodes(root.right)
        return self.all_nodes
        
    def create_tree(self, root, depth):
        if depth == 0:
            return
        node_left = Tree_node()
        node_left.value = random.random()
        node_left.ID = random.randint(0,1000)
        root.set_left(node_left)
        node_right = Tree_node()
        node_right.value = random.random()
        node_right.ID = random.randint(0,1000)
        root.set_right(node_right)
        self.create_tree(node_left, depth-1)
        self.create_tree(node_right, depth-1)
        
    def get_height(self, root):
        if root is None:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1
        
    def is_binary_search_tree(self, root, min_=-np.inf, max_=np.inf):
        if root is None:
            return True
        if root.value <= min_ or root.value > max_:
            return False
        if self.is_binary_search_tree(root=root.left, min_=min_, max_=root.value) and self.is_binary_search_tree(root=root.right, min_=root.value, max_=max_):
            return True
        else:
            return False
        
class Tree_node_binary_search(object):
    def __init__(self, value=None, left=None, right=None, ID=None):
        self.left = left
        self.right = right
        self.value = value
        self.ID = ID
        self.all_IDs = []
        self.all_nodes = []
        
    def set_left(self, node):
        self.left = node
        
    def set_right(self, node):
        self.right = node
        
    def print_tree(self, root):
        if root is None:
            return
        print("ID: {}, value: {}".format(root.ID, root.value))
        self.print_tree(root.left)
        self.print_tree(root.right)
        
    def get_IDs(self, root):
        if root is None:
            return
        self.all_IDs.append(root.ID)
        self.get_IDs(root.left)
        self.get_IDs(root.right)
        return self.all_IDs
    
    def get_nodes(self, root):
        if root is None:
            return
        self.all_nodes.append(root)
        self.get_nodes(root.left)
        self.get_nodes(root.right)
        return self.all_nodes
        
    def create_binary_search_tree(self, root, depth, min_=0, max_=1000):
        if depth == 0:
            return
        node_left = Tree_node()
        value = random.randint(min_+1,root.value-1)
        node_left.value = value
        node_left.ID = value-1
        # node_left.ID = random.randint(0,1000)
        root.set_left(node_left)
        node_right = Tree_node()
        value = random.randint(root.value+1, max_-1)
        node_right.value = value
        node_right.ID = value-1
        # node_right.ID = random.randint(0,1000)
        root.set_right(node_right)
        self.create_binary_search_tree(node_left, depth-1, min_=min_, max_=root.value)
        self.create_binary_search_tree(node_right, depth-1, min_=root.value, max_=max_)
        
    def get_height(self, root):
        if root is None:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1
    
    def is_binary_search_tree(self, root, min_=-np.inf, max_=np.inf):
        if root is None:
            return True
        if root.value <= min_ or root.value > max_:
            return False
        if self.is_binary_search_tree(root=root.left, min_=min_, max_=root.value) and self.is_binary_search_tree(root=root.right, min_=root.value, max_=max_):
            return True
        else:
            return False

if __name__ == '__main__':
    main()