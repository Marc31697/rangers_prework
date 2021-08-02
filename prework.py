def is_consecutive(a_list):
    a_list.sort()
    return a_list == list(range(min(a_list), max(a_list)+1))

print(is_consecutive([2, 1, 3, 4, 5]))



def hello_name(user_name):
    print('hello_' + user_name.upper() + '!')

hello_name('SamsungSmartFridge')

hello_name('CodingTempleUser15')



def leap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 !=0 and year % 400 !=0:
        return True
    else: 
        return False

x = leap(2024)
print(x)



def max_num_in_list(a_list):
    print(max(a_list))


max_num_in_list({60, 22, 57, 110, 123})



def odd_numbers(list):
    for x in list:
        if x % 2 != 0:
            print(x)

odd_numbers(range(0,100))