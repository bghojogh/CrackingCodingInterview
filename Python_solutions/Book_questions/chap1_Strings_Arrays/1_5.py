def main():
    print(convert_string(string_="hello hi"))
    print(convert_string(string_="hello hiiiiiiiiiiiiiii"))
    
def convert_string(string_):
    string_2 = ""
    prev_char_ = string_[0]
    count_ = 1
    for i, char_ in enumerate(string_):
        if i == 0:
            continue
        if char_ == prev_char_:
            count_ += 1
        else:
            string_2 += (prev_char_ + str(count_))
            count_ = 1
        prev_char_ = char_
        if i == len(string_)-1:
            string_2 += (prev_char_ + str(count_))
    if len(string_2) < len(string_):
        return string_2
    else:
        return string_

if __name__ == "__main__":
    main()