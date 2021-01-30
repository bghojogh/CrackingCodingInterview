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
    
    def find_k_th_to_last_element(self, k):
        node_1 = self.head
        node_2 = self.head
        for i in range(k):
            node_2 = node_2.next_node
        while(node_2 != None):
            node_2 = node_2.next_node
            node_1 = node_1.next_node
        return node_1.data
        
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
    print(list1.find_k_th_to_last_element(k=3))
    print(list1.find_k_th_to_last_element(k=5))

if __name__ == '__main__':
    main()