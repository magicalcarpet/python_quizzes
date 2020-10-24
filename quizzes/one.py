# find the largest number in a list

def largest_number(a_list):
    if not isinstance(a_list, list):
        raise Exception(f'Sorry, enter only a list and not a {type(a_list)}')
    a_list.sort()
    return a_list[-1]


result = largest_number([23, 76, 78, 2, 90, 232, -2, 41])
print(result)
