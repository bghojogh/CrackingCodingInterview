# https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def insert_top(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        
    def insert_tail(self, data):
        new_node = Node(data)
        next_ = self.head
        while(next_.next_node != None):
            next_ = next_.next_node
        next_.next_node = new_node
    
    def print_list(self):
        node_ = self.head
        str_ = ""
        while(node_ != None):
            if node_ != self.head:
                str_ += " -> "
            str_ += "{}".format(node_.data)
            node_ = node_.next_node
        print(str_)
    
    def get_k_th_node(self, k):
        node_ = self.head
        for i in range(k):
            node_ = node_.next_node
        return node_
    
    def delete_node_onlyAccessToNode(self, node_):
        node_.data = (node_.next_node).data
        node_.next_node = (node_.next_node).next_node
        
def main():
    list1 = SinglyLinkedList()
    list1.insert_top(1)
    list1.insert_tail(2)
    list1.insert_tail(2)
    list1.insert_tail(3)
    list1.insert_tail(2)
    list1.insert_tail(4)
    list1.insert_tail(4)
    list1.insert_tail(2)
    list1.print_list()
    node_ = list1.get_k_th_node(k=2)
    list1.delete_node_onlyAccessToNode(node_=node_)
    list1.print_list()

if __name__ == '__main__':
    main()