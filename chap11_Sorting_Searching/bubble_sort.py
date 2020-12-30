import numpy as np

def main():
    print(bubble_sort([6,1,9,3,8,10]))

# https://en.wikipedia.org/wiki/Bubble_sort#/media/File:Bubble-sort-example-300px.gif
# https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(array):
    for run in range(len(array)):
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
    return array

# def bubble_sort(array):
#     for run in range(len(array)):
#         for index in range(len(array)-1):
#             if array[index] > array[index+1]:
#                 temp = array[index]
#                 array[index] = array[index+1]
#                 array[index+1] = temp
#     return array
           
if __name__ == '__main__':
    main()