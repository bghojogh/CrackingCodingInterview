#### Question: Task scheduling: Given a set of pins with attributes (pin id, height), 
#### write a function that takes the argument 'k' (determining the number of columns) 
#### and inserts the pins such that every pin goes into a column with least consumed height. 
#### If there is a tie then insert into the left most column.

import numpy as np

def main():
    set_of_pins = [(0,3), (1,10), (2,3), (3,5), (4,12)]
    k = 3
    print(assign_pins_exhaustive(set_of_pins, k))
    print(assign_pins_priority_queue(set_of_pins, k))
    
# output:
# [[(0, 3), (3, 5)], [(1, 10), (4, 12)], [(2, 3)]]
# [[(0, 3), (4, 12)], [(1, 10), (2, 3)], [(3, 5)]]
    
def assign_pins_exhaustive(set_of_pins, k):
    list_ = [[] for i in range(k)]
    for pin in set_of_pins:
        list_ = exhaustive_search(pin, list_)
    return list_

def assign_pins_priority_queue(set_of_pins, k):
    list_ = [[] for i in range(k)]
    list_heights = []
    for pin in set_of_pins:
        pin_height = pin[1]
        list_heights, index_inserted = min_heap_insert(heap_=list_heights, value=pin_height, max_len_heap_=k)
        list_[index_inserted].append(pin)
    return list_
    
def exhaustive_search(pin, list_):
    min_length = np.inf
    min_col_index = None
    for i, col in enumerate(list_):
        col_height = 0
        for pin__ in col:
            col_height += pin__[1]
        if len(col) < min_length:
            min_length = len(col)
            min_col_index = i
    list_[min_col_index].append(pin)
    return list_

def min_heap_insert(heap_, value, max_len_heap_):
    # https://www.youtube.com/watch?v=HqPJF2L5h9U
    if len(heap_) <= max_len_heap_:
        index_inserted = 0
        heap_.append(value)
        index = len(heap_) - 1
        while True:
            index_parent = ceil(index / 2)
            if heap_[index] < heap_[index_parent]:
                heap_[index], heap_[index_parent] = heap_[index_parent], heap_[index]
                index = index_parent
            else:
                index_inserted = index
                break
    else:
        index_inserted = 0
        heap_[0] += value
    return heap_, index_inserted

def min_heap_pop(heap_):
    # https://www.youtube.com/watch?v=HqPJF2L5h9U
    value = heap_[0]
    heap = heap_[1:]
    heap_[0] = heap_[-1]
    while True:
        index_left_child = index * 2
        index_right_child = (index * 2) + 1
        if heap_[index] > heap_[index_left_child]:
            heap_[index], heap_[index_left_child] = heap_[index_left_child], heap[index]
            index = index_left_child
        elif heap_[index] > heap_[index_right_child]:
            heap_[index], heap_[index_right_child] = heap_[index_right_child], heap_[index]
            index = index_right_child
        else:
            break
    return heap_

if __name__ == "__main__":
    main()
