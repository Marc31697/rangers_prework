def odd_numbers(list):
    for x in list:
        if x % 2 != 0:
            print(x)

odd_numbers(range(0,100))