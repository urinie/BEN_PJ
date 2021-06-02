from exception_demo import my_function

try:
    my_function()
except IndexError:
    print("Loi chi muc")
except ZeroDivisionError:
    print("loi chia cho 0!")
finally:
    print("Xong!")