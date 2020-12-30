import numpy as np

def main():
    print(find_magic_index(sorted_A=[0,1,2,5,6]))
    print(find_magic_index(sorted_A=[1,2,3,3,6]))
    
    print(find_magic_index_DISTINCT(sorted_A=[0,1,2,5,6]))
    print(find_magic_index_DISTINCT(sorted_A=[1,2,3,3,6]))

def find_magic_index_DISTINCT(sorted_A, index=0):
    if index == sorted_A[index]:
        return index
    if index < sorted_A[index]:
        return None
    return find_magic_index(sorted_A, index+1)

def find_magic_index(sorted_A, index=0):
    if index == sorted_A[index]:
        return index
    if index > len(sorted_A)-1:
        return None
    return find_magic_index(sorted_A, index+1)
            
if __name__ == '__main__':
    main()