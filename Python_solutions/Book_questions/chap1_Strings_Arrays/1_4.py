def main():
    print(replace_spaces(string_="hello hi"))
    
def replace_spaces(string_):
    chars_modified = [char_ if char_ != " " else "%20" for char_ in string_]
    string_modified = ""
    for char_ in chars_modified:
        string_modified += char_
    return string_modified

if __name__ == "__main__":
    main()