def leap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 !=0 and year % 400 !=0:
        return True
    else: 
        return False

x = leap(2024)
print(x)