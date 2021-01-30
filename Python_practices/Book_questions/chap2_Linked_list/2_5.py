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
    
def add_reverse_order(list1, list2):
    list_add = SinglyLinkedList()
    node1 = list1.head
    node2 = list2.head
    digit_index = 0
    value_10s = 0
    while(node1 != None and node2 != None):
        if node1 == None or node2 == None:
            raise ValueError("no same lengths")
        sum_ = int(node1.data + node2.data + value_10s)
        value = sum_ % 10
        value_10s = floor(sum_ / 10)
        if digit_index == 0:
            list_add.insert_top(value)
        else:
            list_add.insert_tail(value)
        node1 = node1.next_node
        node2 = node2.next_node
        digit_index += 1
    if value_10s != 0:
        list_add.insert_tail(int(value_10s))
    return list_add

def add_forward_order(list1, list2):
    list1.reverse_list()
    list2.reverse_list()
    return add_reverse_order(list1, list2)
        
def main():
    list1 = SinglyLinkedList()
    list1.insert_top(7)
    list1.insert_tail(1)
    list1.insert_tail(6)
    list1.print_list()
    
    list2 = SinglyLinkedList()
    list2.insert_top(5)
    list2.insert_tail(9)
    list2.insert_tail(2)
    list2.print_list()
    
    list3 = add_reverse_order(list1, list2)
    list3.print_list()
    
    print("------------------------")
    list3 = add_forward_order(list1, list2)
    list1.print_list()
    list2.print_list()
    list3.print_list()

if __name__ == '__main__':
    main()