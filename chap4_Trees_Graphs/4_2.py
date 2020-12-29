import numpy as np

def main():
    tree1 = Tree_node()
    tree1.value = 250
    tree1.ID = 360
    tree1.create_tree(tree1, depth=2)
    tree1.print_tree(tree1)
    IDs_tree1 = tree1.get_IDs(tree1)
    print(IDs_tree1)
    nodes_tree1 = tree1.get_nodes(tree1)
    # print(nodes_tree1)
    ########################################
    tree2 = Tree_node()
    tree2.value = 1050
    tree2.ID = 1060
    tree2.create_tree(tree2, depth=2)
    tree2.print_tree(tree2)
    ######################################## Using BFS search:
    print(search_BFS(tree1, tree2))
    print(search_BFS(tree1, nodes_tree1[-1]))
    ######################################## Using DFS search:
    final_desicion, _ = search_DFS(tree1, tree2)
    print(final_desicion)
    final_desicion, _ = search_DFS(tree1, nodes_tree1[-1])
    print(final_desicion)
    
def search_BFS(node1, node2):
    queue = [node1]
    visited = [node1]
    while len(queue) != 0:
        node = queue.pop(0)  #--> dequeue
        for neighbor_node in get_neighbors(node):
            if neighbor_node is not None:
                if neighbor_node not in visited:
                    if neighbor_node == node2:
                        return True
                    visited.append(neighbor_node)
                    queue.append(neighbor_node) #--> enqueue
    return False

def search_DFS(node1, node2, visited=[]):
    if node1 is None:
        return False, visited
    visited.append(node1)
    final_desicion = True
    for neighbor_node in get_neighbors(node1):
        if neighbor_node not in visited:
            if neighbor_node == node2:
                return True, visited
            decision, visited = search_DFS(neighbor_node, node2, visited)
            final_desicion &= decision
    return final_desicion, visited

def get_neighbors(node):
    return [node.left, node.right]

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