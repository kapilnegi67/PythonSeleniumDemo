# try:
#        # Some Code.... 
#
# except:
#        # optional block
#        # Handling of exception (if required)
#
# else:
#        # execute if no exception
#
# finally:
#       # Some code .....(always executed)

x = 2
y = 0
try:
    # Floor Division : Gives only Fractional
    # Part as Answer
    result = x // y
except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")
else:
    print("Yeah ! Your answer is :", result)
finally: 
    # this block is always executed  
    # regardless of exception generation. 
    print('This is always executed')  