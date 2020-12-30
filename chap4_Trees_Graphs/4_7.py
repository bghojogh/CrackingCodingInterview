import numpy as np

def main():
    tree1 = Tree_node()
    tree1.value = 250
    tree1.ID = 360
    tree1.create_tree(tree1, depth=2)
    tree1.print_tree(tree1)
    nodes_tree1 = tree1.get_nodes(tree1)
    print(nodes_tree1)
    print(tree1.find_common_ancestor(node1=nodes_tree1[2], node2=nodes_tree1[4], root=tree1))

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
        
    def is_node_in_subtree_of_root(self, node, root):
        if root is None:
            return False
        if node == root:
            return True
        return self.is_node_in_subtree_of_root(node, root.left) or self.is_node_in_subtree_of_root(node, root.right)
        
    def find_common_ancestor(self, node1, node2, root):
        if root is None:
            return None
        node1_in_left = self.is_node_in_subtree_of_root(node=node1, root=root.left)
        node1_in_right = self.is_node_in_subtree_of_root(node=node1, root=root.right)
        node2_in_left = self.is_node_in_subtree_of_root(node=node2, root=root.left)
        node2_in_right = self.is_node_in_subtree_of_root(node=node2, root=root.right)
        if (node1_in_left and node2_in_right) or (node2_in_left and node1_in_right):
            return root
        elif node1_in_left and node2_in_left:
            self.find_common_ancestor(node1=node1, node2=node2, root=root.left)
        elif node1_in_right and node2_in_right:
            self.find_common_ancestor(node1=node1, node2=node2, root=root.right)
            

if __name__ == '__main__':
    main()