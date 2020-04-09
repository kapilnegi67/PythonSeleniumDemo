def my_decorator(func):
    def my_func_wrapper(func_var):
        print("Start of func wrapper")
        func(func_var)
        print("End of func wrapper")
    return my_func_wrapper


def my_func(func_var):
    print("My func was passed value = ", func_var)


print("Normal Function call")
my_func(func_var="Normal")

print("Decorate my_func with my_decorator")
my_func = my_decorator(my_func)

print("Value after decorator is applied")
my_func(func_var="Decorated")


# Generally Used pattern
print("\n\n\n")

@my_decorator
def my_new_func(func_var):
    print("My new func was passed value = ", func_var)

my_new_func(func_var="New Decorated")
