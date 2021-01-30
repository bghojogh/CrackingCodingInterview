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
        
    def is_palindrome(self):
        values = []
        node_ = self.head
        while(node_ != None):
            values.append(node_.data)
            node_ = node_.next_node
        self.reverse_list()
        # self.print_list()
        node_ = self.head
        counter_ = 0
        while(node_ != None):
            if node_.data != values[counter_]:
                return False
            node_ = node_.next_node
            counter_ += 1
        return True
    
    def is_palindrome_usingStack(self):
        values = []
        node_slow = self.head
        node_fast = self.head
        is_length_odd = False
        while(node_fast != None):
            values.append(node_slow.data)
            node_slow = node_slow.next_node
            if node_fast.next_node != None:
                node_fast = (node_fast.next_node).next_node
            else:
                is_length_odd = True
                break
        if is_length_odd:
            values.pop()
        while(node_slow != None):
            if node_slow.data != values.pop():
                return False
            node_slow = node_slow.next_node
        return True
        
def main():
    list1 = SinglyLinkedList()
    list1.insert_top(7)
    list1.insert_tail(1)
    list1.insert_tail(6)
    list1.insert_tail(5)
    list1.insert_tail(4)
    list1.insert_tail(3)
    list1.print_list()
    print(list1.is_palindrome())
    
    list1 = SinglyLinkedList()
    list1.insert_top(7)
    list1.insert_tail(1)
    list1.insert_tail(6)
    list1.insert_tail(5)
    list1.insert_tail(4)
    list1.insert_tail(3)
    list1.print_list()
    print(list1.is_palindrome_usingStack())
    
    list1 = SinglyLinkedList()
    list1.insert_top(7)
    list1.insert_tail(1)
    list1.insert_tail(6)
    list1.insert_tail(6)
    list1.insert_tail(1)
    list1.insert_tail(7)
    list1.print_list()
    print(list1.is_palindrome())
    
    list1 = SinglyLinkedList()
    list1.insert_top(7)
    list1.insert_tail(1)
    list1.insert_tail(6)
    list1.insert_tail(6)
    list1.insert_tail(1)
    list1.insert_tail(7)
    list1.print_list()
    print(list1.is_palindrome_usingStack())
    
    list1 = SinglyLinkedList()
    list1.insert_top(7)
    list1.insert_tail(1)
    list1.insert_tail(6)
    list1.insert_tail(1)
    list1.insert_tail(7)
    list1.print_list()
    print(list1.is_palindrome())
    
    list1 = SinglyLinkedList()
    list1.insert_top(7)
    list1.insert_tail(1)
    list1.insert_tail(6)
    list1.insert_tail(1)
    list1.insert_tail(7)
    list1.print_list()
    print(list1.is_palindrome_usingStack())

if __name__ == '__main__':
    main()