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
    
    def remove_duplicates(self):
        node_ = self.head
        node_previous = None
        unique_values = set()
        while(node_ != None):
            if node_.data in unique_values:
                node_previous.next_node = node_.next_node
            unique_values.add(node_.data)
            node_previous = node_
            node_ = node_.next_node
        
    def remove_duplicates_without_buffer(self):
        node_1 = self.head
        while(node_1 != None):
            node_previous = node_1
            node_2 = node_1.next_node
            while(node_2 != None):
                if node_2.data == node_1.data:
                    node_previous.next_node = node_2.next_node
                node_previous = node_2
                node_2 = node_2.next_node
            node_1 = node_1.next_node
        
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
    list1.remove_duplicates()
    list1.print_list()
    
    list2 = SinglyLinkedList()
    list2.insert_top(1)
    list2.insert_tail(2)
    list2.insert_tail(2)
    list2.insert_tail(3)
    list2.insert_tail(2)
    list2.insert_tail(4)
    list2.insert_tail(4)
    list2.insert_tail(2)
    list2.print_list()
    list2.remove_duplicates_without_buffer()
    list2.print_list()

if __name__ == '__main__':
    main()