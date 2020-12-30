import numpy as np

def main():
    print(count_ways_recursive(10))
    print(count_ways_DP(10))

def count_ways_recursive(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    return count_ways_recursive(n-1) + count_ways_recursive(n-2) + count_ways_recursive(n-3)

def count_ways_DP(n, array=[0,0,1]):
    if n == 1:
        return 1
    if n < 1:
        return 0
    try:
        if array[n] != 0:
            return array[n]
    except:
        pass
    array.append(count_ways_DP(n-1, array) + count_ways_DP(n-2, array) + count_ways_DP(n-3, array))
    return array[-1]
            
if __name__ == '__main__':
    main()