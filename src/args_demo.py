def add_all(a, *numbers):
    sum = 0

    for number in numbers:
        sum += number

    print("Sum of all the given numbers is : %s" % sum)

add_all(1,2,3,4,5,6,7,8)

add_all(1,2,3,4,5,6,7,8,5,1,5,0)