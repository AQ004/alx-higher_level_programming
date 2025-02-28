def remove_char_at(str, n):
    string_list = list(str)
    string_list.pop(n)
    string = "".join(string_list)
    return string
