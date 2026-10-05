def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


my_year = 2024
result = is_year_leap(my_year)
print("год", my_year, ":", result)
