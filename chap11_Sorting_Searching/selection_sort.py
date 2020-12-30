import numpy as np

def main():
    print(selection_sort([6,1,9,3,8,10]))

# https://en.wikipedia.org/wiki/File:Selection-Sort-Animation.gif
# https://en.wikipedia.org/wiki/Selection_sort
def selection_sort(array):
    for index in range(len(array)):
        min_ = array[index]
        min_loc = index
        for index2 in range(index+1, len(array)):
            if array[index2] < min_:
                min_ = array[index2]
                min_loc = index2
        array[index], array[min_loc] = min_, array[index]
    return array

# def selection_sort(array):
#     for index in range(len(array)):
#         min_ = array[index]
#         min_loc = index
#         for index2 in range(index+1, len(array)):
#             if array[index2] < min_:
#                 min_ = array[index2]
#                 min_loc = index2
#         temp = array[index]
#         array[index] = min_
#         array[min_loc] = temp
#     return array
            
if __name__ == '__main__':
    main()