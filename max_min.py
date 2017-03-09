def find_max_min(list_of_arguments):
    """
    This is a function that returns the minimum and maximum value of the list provided
    if the maximum and minimum value are equal the length of the list is returned.
    """
   list_output = []
  for values in list_of_arguments:
    min_value = min(list_of_arguments)
    max_value = max(list_of_arguments)
  if max_value == min_value:
    list_output.append(len(list_of_arguments))
  else:
    list_output.insert(0, min_value)
    list_output.insert(1, max_value)
  return list_output