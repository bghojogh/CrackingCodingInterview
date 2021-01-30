#### Question: Given an input string which is the output of a count and say method, 
#### return the original number. For example: If the number if "21", then the count and say method 
#### would return "1211" (one two, one one). In this problem, 
#### the input provided to us is "1211" and our goal is to return "21".

def main():
    list_ = "1211"
    print(reverse_count_and_say(list_))
    
    list_ = "1211342178"
    print(reverse_count_and_say(list_))
    
# output:
# 21
# 21444118888888
    
def reverse_count_and_say(list_):
    if len(list_) % 2 != 0:
        raise ValueError("Not a valid string!")
    string_ = ""
    for index in range(len(list_) // 2):
        a, b = list_[index*2], list_[(index*2)+1]
        string_ += int(a) * b
    return string_

if __name__ == "__main__":
    main()
