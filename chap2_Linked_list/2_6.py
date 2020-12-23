# it needs to be completed... (see solution of pages 195-196 in the book)

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
        
    def make_loop(self, node_index_as_start_of_loop):
        node_ = self.head
        counter_ = 0
        while(node_.next_node != None):
            if counter_ == node_index_as_start_of_loop:
                start_loop_node = node_
            node_ = node_.next_node
            counter_ += 1
        # node_.set_next(start_loop_node)
        self.insert_tail(start_loop_node.data)
    
    def print_list(self):
        node_ = self.head
        str_ = ""
        while(node_ != None):
            if node_ != self.head:
                str_ += " -> "
            str_ += "{}".format(node_.data)
            node_ = node_.next_node
        print(str_)
        
    def reverse_list(self):
        # https://www.geeksforgeeks.org/reverse-a-linked-list/
        current_node = self.head
        previous_node = None
        while(current_node != None):
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
        
def main():
    list1 = SinglyLinkedList()
    list1.insert_top(7)
    list1.insert_tail(1)
    list1.insert_tail(6)
    list1.insert_tail(5)
    list1.insert_tail(4)
    list1.insert_tail(3)
    list1.make_loop(node_index_as_start_of_loop=2)
    list1.print_list()
    

if __name__ == '__main__':
    main()