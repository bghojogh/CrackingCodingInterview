def main():
    print(reverse_string(string_="hello hi"))

def reverse_string(string_):
    reveresed = ''
    for char_ in reversed(string_):
        reveresed += char_
    return reveresed

if __name__ == "__main__":
    main()
