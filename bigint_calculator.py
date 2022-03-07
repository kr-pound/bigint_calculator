# receive 2 numbers as string, and compute the added value
# add(str_A, str_B) --> str_result
def add(bigintA, bigintB):
    
    #set as initial and addend, with 0 carry digit
    initial = int(bigintA)
    addend = int(bigintB)
    carry = 0

    add_temp = 0
    result = ""

    # add the last digit of each int, then, delete that digit
    while(initial > 0 or addend > 0 or carry > 0):
        # save the added value in add_temp
        add_temp = (initial % 10) + (addend % 10) + carry

        # reset carry digit to 0
        carry = 0

        # assign last digit of add_temp to be in front of result string
        # and delete that digit
        result = str(add_temp % 10) + result
        add_temp //= 10

        # if the add_temp still left, assign to carry for the next digit
        # and reset add_temp
        if (add_temp > 0):
            carry = add_temp
            add_temp = 0

        # delete the last digit of initial and addend
        initial //= 10
        addend //= 10

    return result
    


bigintA = input("Input A: ")
bigintB = input("Input B: ")

print("A + B =", add(bigintA, bigintB))


