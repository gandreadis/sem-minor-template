from project.leap_year_checker import is_leap_year

year = input("Enter a year number: ")
print("Is", year, "a leap year?", is_leap_year(int(year)))
