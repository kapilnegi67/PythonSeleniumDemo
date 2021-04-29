a = int(input("Enter a dividend: "))

try:
    if a == 0:
        raise ZeroDivisionError("Can not divide by number 0")
        # raise ValueError("That is not a positive number!")
except ZeroDivisionError as ve:
    print(ve)