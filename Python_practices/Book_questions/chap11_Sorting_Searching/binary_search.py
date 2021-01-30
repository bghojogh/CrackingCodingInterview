import numpy as np

def main():
    arr = [6,1,9,3,1,8,10]
    print(arr)
    print(binary_search(arr, value=9))

def binary_search(arr, value, args=None):
    if args is None:
        args = [i for i in range(len(arr))]
    if not check_is_sorted(arr):
        arr, args = bubble_sort(arr)
    mid_index = len(arr) // 2
    mid = arr[mid_index]
    if len(arr) <= 1:
        return None
    if value == mid:
        return args[mid_index]
    elif value < mid:
        return binary_search(arr[:mid_index], value, args)
    else:
        return binary_search(arr[mid_index:], value, args)
    
def check_is_sorted(arr):
    for index in range(len(arr)-1):
        if arr[index] > arr[index+1]:
            return False
    return True
    
def bubble_sort(array):
    indices = [i for i in range(len(array))]
    for run in range(len(array)):
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                indices[index], indices[index+1] = indices[index+1], indices[index]
    return array, indices
    
if __name__ == '__main__':
    main()