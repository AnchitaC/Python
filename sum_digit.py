                                                                                                                                                             
n = raw_input("Please enter a number: ")

def digit_sum(n):
    total = 0
    for char in str(n):
        total = total + int(char)
    print "total of " + str(n) + " is " + str(total)
    return total

digit_sum(n)

