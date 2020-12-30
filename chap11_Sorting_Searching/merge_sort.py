import numpy as np

def main():
    print(mergeSort([6,1,9,3,8,10]))

# https://www.geeksforgeeks.org/merge-sort/
# https://en.wikipedia.org/wiki/File:Merge-sort-example-300px.gif
# https://en.wikipedia.org/wiki/Merge_sort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    # Finding the mid of the array
    mid = len(arr)//2

    # Dividing the array elements
    L = arr[:mid]

    # into 2 halves
    R = arr[mid:]

    # Sorting the first half
    mergeSort(L)

    # Sorting the second half
    mergeSort(R)

    ################ merge:
    i = j = k = 0
    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    #---> no need to this really:
    # while j < len(R):
    #     arr[k] = R[j]
    #     j += 1
    #     k += 1
    
    return arr
            
if __name__ == '__main__':
    main()