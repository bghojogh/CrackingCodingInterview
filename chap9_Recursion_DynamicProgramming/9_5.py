import numpy as np

def main():
    print(permutations(s="hello"))

# https://stackoverflow.com/questions/13109274/python-recursion-permutations
def permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for e in permutations(s[:-1]):
            for i in xrange(len(e)+1):
                perms.append(e[:i] + s[-1] + e[i:])
        return perms
            
if __name__ == '__main__':
    main()