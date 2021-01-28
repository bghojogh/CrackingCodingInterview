import numpy as np

def main():
    tree = Tree_node()
    tree.value = 250
    tree.ID = 360
    tree.create_tree(tree, depth=4)
    tree.print_tree(tree)
    print(tree.is_balanced(tree))
    tree.add_left_subtree(tree, depth_sub_tree=3)
    print(tree.is_balanced(tree))

class Tree_node(object):
    def __init__(self, value=None, left=None, right=None, ID=None):
        self.left = left
        self.right = right
        self.value = value
        self.ID = ID
        
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
    
    def is_balanced(self, root):
        if root is None:
            return True
        diff = abs(self.get_height(root.left) - self.get_height(root.right))
        if diff > 1:
            return False
        else:
            return self.is_balanced(root.left) and self.is_balanced(root.right)

if __name__ == '__main__':
    main()