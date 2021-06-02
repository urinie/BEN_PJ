from exception_demo import my_function

try:
    my_function()
except IndexError:
    print("Exception index")
except ZeroDivisionError:
    print("The number 2 should not be 0")
except Exception as e:
    print(e)