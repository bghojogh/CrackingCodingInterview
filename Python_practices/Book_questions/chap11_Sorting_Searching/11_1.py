import numpy as np

def main():
    arr1 = [5,7,10,11]
    arr2 = [1,5,6,10,11,12,13]
    print(merge(arr1, arr2))

def merge(arr1, arr2):
    for i2 in range(len(arr2)):
        flag = True
        for i1 in range(len(arr1)):
            if arr2[i2] < arr1[i1]:
                arr1 = arr1[:i1] + [arr2[i2]] + arr1[i1:]
                flag = False
                break
        if flag:
            arr1 = arr1 + [arr2[i2]]
    return arr1
    
if __name__ == '__main__':
    main()