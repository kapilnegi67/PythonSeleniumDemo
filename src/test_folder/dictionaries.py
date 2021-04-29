my_dict = {"A": 1, "B":2, "C": 3, "D": 4}

my_dict2 = my_dict
my_dict3 = my_dict.copy()

my_dict["A"] = 5

print(my_dict2)
print(my_dict3)

