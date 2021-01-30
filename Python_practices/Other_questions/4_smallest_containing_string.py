# Question: Find the smallest string which has the Alphabet in order.
# Input: "bAjkAcbqADBdop[sDbBAcCDgdChDhqAB"
# Alphabet=["A","B","C","D"]
# output: "ADBdop[sDbBAcCD"

def main():
    Input = "bAjkAcbqADBdop[sDbBAcCDgdChDhqAB"
    # Input = "bAABCAD"
    Alphabet = ["A","B","C","D"]
    
    ##### BFS solution:
    sucess, string_ = find_shortest_string_BFS(string_=Input, Alphabet=Alphabet)
    print(sucess)
    print(string_)
    
    ##### DFS solution:
    sucess, string_ = find_shortest_string_DFS(string_, Alphabet)
    print(sucess)
    print(string_)
    
    # ##### recursive solution: --> not working well
    # sucess, string_ = find_shortest_string_recursion(string_=Input, Alphabet=Alphabet)
    # print(sucess)
    # print(string_)
    
# output of code:
# True
# ADBdop[sDbBAcCD
# True
# ADBdop[sDbBAcCD

def find_shortest_string_DFS(string_, Alphabet, root_index=0):
    if root_index > len(string_) - 1:
        return False, string_
    # visit the string starting from root_index:
    answer_ = string_
    answer_sucess = False
    sucess1, string_containing1 = is_Alphabet_in_string(string_[root_index:], Alphabet)
    if sucess1:
        answer_ = string_containing1
        answer_sucess = True
    if root_index < len(string_) - 1:
        root_index = root_index + 1
        sucess2, string_containing2 = find_shortest_string_DFS(string_, Alphabet, root_index)
    else:
        sucess2 = False
    if sucess1 and (not sucess2):
        answer_ = string_containing1
        answer_sucess = True
    elif (not sucess1) and (sucess2):
        answer_ = string_containing2
        answer_sucess = True
    elif (sucess1) and (sucess2):
        if len(string_containing1) < len(string_containing2):
            answer_ = string_containing1
            answer_sucess = True
        else:
            answer_ = string_containing2
            answer_sucess = True
    else:
        answer_ = None
        answer_sucess = False
    return answer_sucess, answer_
    
def find_shortest_string_BFS(string_, Alphabet):
    queue_ = []
    root_index=0
    queue_.append(root_index)
    # visit the string starting from root_index:
    answer_ = string_
    answer_sucess = False
    sucess, string_containing = is_Alphabet_in_string(string_[root_index:], Alphabet)
    if sucess:
        answer_ = string_containing
        answer_sucess = True
    while len(queue_) != 0:
        index = queue_[0]
        queue_ = queue_[1:] #--> dequeue
        if root_index < len(string_) - 1:
            root_index = index + 1
        else:
            break
        sucess, string_containing = is_Alphabet_in_string(string_[root_index:], Alphabet)
        if sucess:
            if len(string_containing) < len(answer_):
                answer_ = string_containing
                answer_sucess = True
        queue_.append(root_index) #--> enqueue
    return answer_sucess, answer_
    
def is_Alphabet_in_string(string_, Alphabet):
    i = 0
    found_indices = []
    for alphabet in Alphabet:
        found_alphabet = False
        for char_index in range(i, len(string_)):
            char_ = string_[char_index]
            if char_ == alphabet:
                i = char_index + 1
                found_alphabet = True
                found_indices.append(char_index)
                break
        if not found_alphabet:
            return False, None
    string_containing = string_[found_indices[0]:found_indices[-1]+1]
    return True, string_containing

def find_shortest_string_recursion(string_, Alphabet):
    ############### base of recursion:
    if len(string_) <= 1:
        return False, string_
    ############### check if the input string (in recursion) has the Alphabet in order:
    i = 0
    for alphabet in Alphabet:
        found_alphabet = False
        for char_index in range(i, len(string_)):
            char_ = string_[char_index]
            if char_ == alphabet:
                i = char_index + 1
                found_alphabet = True
                break
        if found_alphabet == False:
            return False, string_
    ############### recursion into sub-strings:
    for char_index in range(len(string_)):
        found_in_sub_string1, sub_string1 = find_shortest_string_recursion(string_[:char_index], Alphabet)
        found_in_sub_string2, sub_string2 = find_shortest_string_recursion(string_[char_index:], Alphabet)
    ############### return shortest string_ containing Alphabet in order:
    if (found_alphabet) and (not found_in_sub_string1) and (not found_in_sub_string2):
        return True, string_
    elif (not found_alphabet) and (found_in_sub_string1) and (not found_in_sub_string2):
        return True, sub_string1
    elif (not found_alphabet) and (not found_in_sub_string1) and (found_in_sub_string2):
        return True, sub_string2
    elif (found_alphabet) and (found_in_sub_string1) and (not found_in_sub_string2):
        if len(string_) < len(sub_string1):
            return True, string_
        else:
            return True, sub_string1
    elif (found_alphabet) and (not found_in_sub_string1) and (found_in_sub_string2):
        if len(string_) < len(sub_string2):
            return True, string_
        else:
            return True, sub_string2
    elif (not found_alphabet) and (found_in_sub_string1) and (found_in_sub_string2):
        if len(sub_string1) < len(sub_string2):
            return True, sub_string1
        else:
            return True, sub_string2
    elif (found_alphabet) and (found_in_sub_string1) and (found_in_sub_string2):
        list_ = [len(string_), len(sub_string1), len(sub_string2)]
        if argmin(list_) == 0:
            return True, string_
        elif argmin(list_) == 1:
            return True, sub_string1
        elif argmin(list_) == 2:
            return True, sub_string2
    else:
        return False, string_
        
if __name__ == '__main__':
    main()