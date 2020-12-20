import numpy as np

def main():
    print(are_all_chars_unique(string_="hi, how?"))
    print(are_all_chars_unique(string_="hi?"))
    print(are_all_chars_unique(string_="Hih?", case_matters=False))
    print(are_all_chars_unique(string_="Hih?", case_matters=True))

def are_all_chars_unique(string_, case_matters=False):
    chars_ = []
    if not case_matters: 
        string_ = string_.lower()
    for char_ in string_:
        chars_.append(ord(char_))
    chars_ = np.asarray(chars_)
    return len(np.unique(chars_)) == len(chars_)

if __name__ == "__main__":
    main()
