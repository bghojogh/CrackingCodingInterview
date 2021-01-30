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
    
    def parition(self, x):
        list_before = SinglyLinkedList()
        list_after = SinglyLinkedList()
        node_ = self.head
        count_before = 0
        count_after = 0
        while(node_ != None):
            if node_.data < x:
                if count_before == 0:
                    list_before.insert_top(node_.data)
                else:
                    list_before.insert_tail(node_.data)
                count_before += 1
            else:
                if count_after == 0:
                    list_after.insert_top(node_.data)
                else:
                    list_after.insert_tail(node_.data)
                count_after += 1
            node_ = node_.next_node
        return self.merge_lists(list_before, list_after)
        
    def merge_lists(self, list1, list2):
        list3 = SinglyLinkedList()
        node1 = list1.head
        while(node1 != None):
            if node1 == list1.head:
                list3.insert_top(node1.data)    
            else:
                list3.insert_tail(node1.data)
            node1 = node1.next_node
        node2 = list2.head
        while(node2 != None):
            list3.insert_tail(node2.data)
            node2 = node2.next_node
        return list3
        
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
    list2 = list1.parition(x=3)
    list2.print_list()
    list2 = list1.parition(x=4)
    list2.print_list()

if __name__ == '__main__':
    main()