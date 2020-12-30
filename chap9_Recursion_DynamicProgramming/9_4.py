import numpy as np

def main():
    print(find_subsets(set_=[0,1,2,5,6]))

# https://stackoverflow.com/questions/26332412/python-recursive-function-to-display-all-subsets-of-given-set
def find_subsets(set_):
    if set_ == []:
        return [[]]
    x = find_subsets(set_[1:])
    return x + [[set_[0]] + y for y in x]
            
if __name__ == '__main__':
    main()