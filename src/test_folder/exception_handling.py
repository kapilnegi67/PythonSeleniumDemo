import sys

randomList = [1, 0, 2]

for mem in randomList:
    print(1/mem)
#
# handle error in above code
for mem in randomList:
    try:
        print(1/mem)
    except Exception:
        pass


# Handling specific exception (Positive Example)
for mem in randomList:
    try:
        print(1/mem)
    except ZeroDivisionError:
        pass
#
# Handling specific exception (Negative Example)
for mem in randomList:
    try:
        print(1/mem)
    except TypeError:
        pass
#
# Handling multiple exception
randomList = ['b', 0, 2]
for mem in randomList:
    try:
        print(1/mem)
    except (TypeError,ZeroDivisionError):
        pass