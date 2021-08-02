def is_consecutive(a_list):
    a_list.sort()
    return a_list == list(range(min(a_list), max(a_list)+1))

print(is_consecutive([2, 1, 3, 4, 5]))