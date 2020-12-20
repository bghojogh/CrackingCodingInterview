def main():
    print(is_permutation(string1="hello hi", string2="ih"))
    print(is_permutation(string1="hello hi", string2="ih lohel"))
    print(is_permutation(string1="hello hi", string2="ihlohel"))
    print(is_permutation(string1="hello hi", string2="ih Lohel", case_matters=False))
    print(is_permutation(string1="hello hi", string2="ih Lohel", case_matters=True))

def is_permutation(string1, string2, case_matters=False):
    if not case_matters:
        string1 = string1.lower()
        string2 = string2.lower()
    if len(string1) != len(string2):
        return False
    for char1 in string1:
        if char1 not in string2:
            return False
    for char2 in string2:
        if char2 not in string1:
            return False
    return True

if __name__ == "__main__":
    main()