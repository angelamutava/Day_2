def word(argument):
    """
    This is function that returns the count of words in a string
    """
    string_list = argument.split()
    string_dict = {}
    for word in string_list:
        if word.isdigit():
            word = int(word)
        if word in string_dict:
            string_dict[word] += 1
        else:
            string_dict[word] = 1
    return string_dict