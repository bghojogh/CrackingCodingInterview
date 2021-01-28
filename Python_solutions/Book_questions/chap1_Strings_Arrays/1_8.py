import numpy as np
    
def main():
    s1 = "hello"
    s2 = "lo"
    print(isSubstring(s2, s1))
    
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(isRotation(s2, s1))
    
    s1 = "waterbottle"
    s2 = "erbowatttle"
    print(isRotation(s2, s1))
    
def isSubstring(s1, s2):
    return s1 in s2

def isRotation(s1, s2):
    return isSubstring(s2, s1+s1)
            
if __name__ == "__main__":
    main()