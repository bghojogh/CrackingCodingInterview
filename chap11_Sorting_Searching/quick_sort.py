import numpy as np

def main():
    print(quickSort([6,1,9,3,1,8,10]))

# https://www.geeksforgeeks.org/python-program-for-quicksort/
# https://www.geeksforgeeks.org/quick-sort/
# https://www.youtube.com/watch?v=PgBzjlCcFvc
def quickSort(arr, low=None, high=None): 
    if len(arr) == 1: 
        return arr 
    if low is None: #--> initial call of function in recursion
        low = 0
    if high is None: #--> initial call of function in recursion
        high = len(arr)-1
    if low < high: 
        # pi is partitioning index, arr[p] is now at right place 
        pi = partition(arr, low, high) 
        # Separately sort elements before partition and after partition 
        arr = quickSort(arr, low, pi-1) 
        arr = quickSort(arr, pi+1, high) 
    return arr
        
def partition(arr, low, high): 
    i = (low-1)         # index of smaller element 
    pivot = arr[high]     # pivot 
    for j in range(low, high): 
        # If current element is smaller than or equal to pivot 
        if arr[j] <= pivot: 
            # increment index of smaller element 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
            
if __name__ == '__main__':
    main()