def find_max_min(list_of_arguments):
    """
    This is a function that returns the minimum and maximum value of the list provided
    if the maximum and minimum value are equal the length of the list is returned.
    """
    max_value = list_of_arguments[0]
    min_value = list_of_arguments[1]
    for i in list_of_arguments:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i
        if max_value == min_value:
            return [len(list_of_arguments)]
    return [min_value, max_value]

print(find_max_min([600, 600]))